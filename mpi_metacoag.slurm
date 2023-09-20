#!/bin/bash -l
#SBATCH --account=director2187
#SBATCH --job-name=metacoag_mpi
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --exclusive
#SBATCH --time=1:00:00

module load py-mpi4py/3.1.4-py3.10.10

srun python mpi_metacoag_node.py
