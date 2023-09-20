import shlex
import subprocess 
from mpi4py import MPI

# metacoag command per rank
def run_metacoag(folder_name, rank):
    
    print("Processing at rank", rank, "and reading data from folder:", folder_name)
    
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
            + " --nthreads 4"
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
    
    input_folders = ["5G", "10G", "20G"]  # List of input folders

    if size != len(input_folders):
        if rank == 0:
            print("Number of processes must be equal to the number of files.")
        MPI.Finalize()
        exit()

    folder_name = input_folders[rank]  # Each process gets a unique folder

    # Read and process the assigned folder
    results = run_metacoag(folder_name, rank)

    # Gather results from all processes
    all_results = comm.gather(results, root=0)

    if rank == 0:

        # Process the gathered results (e.g., combine or analyze)
        final_result = sum(all_results)
        print("Total number of bins produced:", final_result)
