# binMPI: MPI-based metagenomic binning

As part of the [PaCER Hackathon 2023](https://github.com/PawseySC/pacer-hackathon-2023) I set out to learn the message passing interface (MPI) and see if I can apply it to distribute and bin multiple metagenomes. Here is the basic idea of my project. Rather than rewriting my code to distribute chunks of one dataset, I wanted to distribute one dataset per node using MPI, do the binning, gather the results and do some statistics.

<p align="center">
  <img src="https://raw.githubusercontent.com/Vini2/binMPI/master/MPI_binning.png" width="800">
</p>

## Setting up MPI

Make sure you have a working MPI implementation like [MPICH](https://www.mpich.org/) or [OpenMPI](https://docs.open-mpi.org/en/v5.0.x/index.html).

## Setting up `mpi4py`

As my code was in python, I used the MPI python interface [`mpi4py`](https://mpi4py.readthedocs.io/en/stable/index.html) which you can install as explained [here](https://mpi4py.readthedocs.io/en/stable/install.html). Make sure to match the compatible mpi4py version to the MPI version you have. I highly recommend staying away from prebuilt version and building from source.

## Setting up `metacoag`

I downloaded the source code of `metacoag` from GitHub and installed it using pip locally.

```
git clone https://github.com/Vini2/MetaCoAG.git
cd MetaCoAG/
pip install -e .
```

