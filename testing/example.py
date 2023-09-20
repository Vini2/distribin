from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    string = "hello"
    datap = [string.encode('utf-8'), MPI.CHAR]
    comm.Send(datap, dest=1, tag=11)
elif rank == 1:
    buf = bytearray(256)
    comm.Recv([buf, MPI.CHAR], source=0, tag=11)
    print("Received", buf.decode('utf-8'))

