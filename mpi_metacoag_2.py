import shlex
import subprocess 
from mpi4py import MPI

# metacoag command per rank
def run_metacoag(folder_name, rank):
    
    print("Processing at rank", rank, MPI.Get_processor_name(), "and reading data from folder:", folder_name)
    
    # metacoag command
    metacoag_cmd = (
            "metacoag --assembler spades"
            + " --graph "
            + folder_name + "/assembly_graph_with_scaffolds.gfa"
            + " --contigs "
            + folder_name + "/contigs.fasta"
            + " --paths "
            + folder_name + "/contigs.paths"
            + " --abundance "
            + folder_name + "/abundance.tsv"
            + " --output "
            + folder_name + "/"
            + " --nthreads 8"
        )
    
    # print(metacoag_cmd)
    
    # run command
    subprocess.run(shlex.split(metacoag_cmd))

    # get number of bins
    n_bins = int(subprocess.check_output([f"ls {folder_name}/bins | wc -l"], shell=True))
    print(n_bins, "bins produced by rank", rank, "for folder", folder_name)

    # return number of bins 
    return n_bins


if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    print("rank:", rank)
    print("size:", size)

    if rank == 0:
        input_folders = ["/scratch/director2187/vmall/mpi_test/5G", 
                         "/scratch/director2187/vmall//mpi_test/10G"]  # List of input folders

        # Scatter the folders
        for i in range(1, size):
            datap = [input_folders[i].encode('utf-8'), MPI.CHAR]
            comm.Send(datap, dest=1, tag=11)

    # Receive the folder
    if rank == 0:
        received_data = input_folders[0]
    else:
        buf = bytearray()
        comm.Recv([buf, MPI.CHAR], source=0, tag=11)
        received_data = buf.decode('utf-8')

    # Process the received folder
    results = run_metacoag(received_data, rank)

    # # Gather the number of bins from all processes
    # all_results = comm.Gather(results, root=0)


    # if rank == 0:

    #     # Process the gathered results
    #     final_result = sum(all_results)
    #     print("Total number of bins produced:", final_result)


