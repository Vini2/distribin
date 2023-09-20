#!/bin/bash -l
#SBATCH --account=director2187
#SBATCH --job-name=metacoag_mpi
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --exclusive
#SBATCH --time=1:00:00

module load py-mpi4py/3.1.4-py3.10.10

# export OMPI_MCA_pml="ucx"
# export OMPI_MCA_osc="ucx"

# mpirun -n 2 python mpi_metacoag_2.py

srun python mpi_metacoag_2.py
