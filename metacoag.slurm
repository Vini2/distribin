#!/bin/bash
#SBATCH --job-name=metacoag_slurm
#SBATCH --time=7-0
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=512G
#SBATCH --array=0-1
#SBATCH -o metacoag-%j.out
#SBATCH -e metacoag-%j.err

gl=(*/assembly_graph_with_scaffolds.gfa)
cl=(*/contigs.fasta)
pl=(*/contigs.paths)
al=(*/abundance.tsv)
ol=(*/)

gf=${gl[$SLURM_ARRAY_TASK_ID]}
cf=${cl[$SLURM_ARRAY_TASK_ID]}
pf=${pl[$SLURM_ARRAY_TASK_ID]}
af=${al[$SLURM_ARRAY_TASK_ID]}
of=${ol[$SLURM_ARRAY_TASK_ID]}

echo $of

metacoag --assembler spades --graph $gf --contigs $cf --paths $pf --abundance $af --nthreads 32 --output $of