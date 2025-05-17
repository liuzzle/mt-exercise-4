# Set paths
base=$(dirname "$0")/..
data=$base/data
sampled_data=$base/sampled_data

mkdir -p $sampled_data

# Sub-sample to 100k lines
head -n 100000 $data/train.de-it.de > $sampled_data/train.de-it.de
head -n 100000 $data/train.de-it.it > $sampled_data/train.de-it.it 

# Copy dev and test sets
cp $data/dev.de-it.de $sampled_data/dev.de-it.de
cp $data/dev.de-it.it $sampled_data/dev.de-it.it
cp $data/test.de-it.de $sampled_data/test.de-it.de
cp $data/test.de-it.it $sampled_data/test.de-it.it

echo "Sub-sampling complete: 100k de-it sentence pairs in $sampled_data"