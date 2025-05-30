#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

models=$base/models
configs=$base/configs

mkdir -p $models_bpe_2k

num_threads=4

# measure time

SECONDS=0

logs=$base/logs

model_name="transformer_sample_config"

mkdir -p $logs

mkdir -p $logs/$model_name

OMP_NUM_THREADS=$num_threads python -m joeynmt train $configs/$model_name.yaml > $logs/$model_name/out_bpelvl_2k_v2 2> $logs/$model_name/err_bpelvl_2k_v2

echo "time taken:"
echo "$SECONDS seconds"
