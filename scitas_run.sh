#!/bin/bash
#
#SBATCH --job-name=alonso
#
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=gpu
#SBATCH --qos=gpu_free
#SBATCH --gres=gpu:1
#SBATCH --mem=30000
#SBATCH --time=12:00:00

python trainSSL_domain_adaptation_targetCity.py --config ./configs/configSSDA.json 