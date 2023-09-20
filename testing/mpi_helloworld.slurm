#!/bin/bash -l
#SBATCH --account=director2187
#SBATCH --job-name=helloworld_mpi
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --exclusive
#SBATCH --time=1:00:00

module load py-mpi4py/3.1.4-py3.10.10
module load py-numpy/1.23.4

srun python example.py
