from time import sleep
import os
import sys
import contextlib
import subprocess
import time
import re
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, choices=['llama', 'bloom'], default='llama')
parser.add_argument('--framework', type=str, choices=['pytorch', 'onnxruntime', 'tensorrt', 'welder', 'vllm', 'vllm_fp16_int4', 'ladder', 'ladder_fp16_int4', 'ladder_fp16_nf4', 'ladder_fp8_fp8', 'ladder_fp16_mxfp8xmxfp8', 'ladder_fp16_int8xint1'], default='pytorch')
parser.add_argument('--batch_size', type=int, default=1)
parser.add_argument('--seq_len', type=int, default=1)
args = parser.parse_args()

model = args.model
framework = args.framework
batch_size = args.batch_size
seq_len = args.seq_len

pwd = os.getcwd()

CHECKPOINT_PATH = os.path.join(os.getcwd(), "../checkpoints/Figure8")

# MODEL_PATH=$(pwd)/../models
model_path = f'{pwd}/../models'

def analyze_log(log_path):
    if not os.path.exists(log_path):
        print(f"{log_path} does not exists")
    peak = 0
    with open(log_path, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            if 'MiB' in line:
                try:
                    peak = max(peak, int(re.split(' ',line)[0]))
                except Exception as err:
                    pass
    return peak

def pytorch_inference(model='llama', batch_size=1, seq_len=1):
    run_file = 'llama_70b.py' if model == 'llama' else 'bloom_176b.py'
    target_process = subprocess.Popen(f'cd {pwd}/pytorch-inductor-benchmark; python {run_file} --batch_size {batch_size} --seq_len {seq_len}; cd ..', shell=True)
    return target_process

def onnxruntime_inference(model='llama', batch_size=1, seq_len=1):
    run_file = 'ort_runtime.py'
    if model=='llama':
        model_file = f'{model_path}/llama_70b/llama-70b_layer1_seq{seq_len}_bs{batch_size}/model.onnx'
    else:
        model_file = f'{model_path}/bloom_176b/bloom-176b_seq{seq_len}_bs{batch_size}/model.onnx'
    target_process = subprocess.Popen(f'cd {pwd}/onnxruntime-benchmark; python {run_file} --file {model_file} --iters 10000 ; cd ..', shell=True)
    return target_process

def tensorrt_inference(model='llama', batch_size=1, seq_len=1):
    # TRT_EXEC_PATH=$(pwd)/../../baseline_framework/TensorRT-9.0.1.4/bin
    trt_exec_path = f'{pwd}/../../baseline_framework/TensorRT-9.0.1.4/bin/trtexec'
    if model=='llama':
        model_file = f'{model_path}/llama_70b/llama-70b_layer1_seq{seq_len}_bs{batch_size}/model.trt'
    else:
        model_file = f'{model_path}/bloom_176b/bloom-176b_seq{seq_len}_bs{batch_size}/model.trt'
    target_process = subprocess.Popen(f'{trt_exec_path} --loadEngine {model_file} --fp16 --workspace=8192 --iterations=10000 ;', shell=True)
    return target_process

def vllm_inference(model='llama', batch_size=1, seq_len=1):
    run_file = 'benchmark_llama.py' if model == 'llama' else 'benchmark_bloom.py'
    target_process = subprocess.Popen(f'cd {pwd}/vllm-benchmark; python {run_file}  --batch_size {batch_size} --seq_len {seq_len}; cd ..', shell=True)
    return target_process

def vllm_fp16_int4_inference(model='llama', batch_size=1, seq_len=1):
    run_file = 'benchmark_llama.py' if model == 'llama' else 'benchmark_bloom.py'
    target_process = subprocess.Popen(f'cd {pwd}/vllm-benchmark; python {run_file}  --batch_size {batch_size} --seq_len {seq_len}; cd ..', shell=True)
    return target_process

def welder_inference(model='llama', batch_size=1, seq_len=1):
    run_file = 'ort_runtime.py'
    if model=='llama':
        model_file = f'{model_path}/llama_70b/llama-70b_layer1_seq{seq_len}_bs{batch_size}/model.onnx'
    else:
        model_file = f'{model_path}/bloom_176b/bloom-176b_seq{seq_len}_bs{batch_size}/model.onnx'
    target_process = subprocess.Popen(f'cd {pwd}/onnxruntime-benchmark; python {run_file} --file {model_file} --iters 10000 ; cd ..', shell=True)
    return target_process

def ladder_inference(model='llama', batch_size=1, seq_len=1):
    run_file = 'ladder_with_fake_dense_dequantize.py'
    if model=='llama':
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/llama_70b/llama2_bs{batch_size}_seq{seq_len}_async'
    else:
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/bloom_176b/llama2_bs{batch_size}_seq{seq_len}_async'
    target_process = subprocess.Popen(f'cd {pwd}/ladder-benchmark; python {run_file} --prebuilt_path {model_file} ; cd ..', shell=True)
    return target_process

def ladder_fp16_int4_inference(model='llama', batch_size=1, seq_len=1):
    run_file = 'ladder_with_fake_dense_dequantize.py'
    if model=='llama':
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/llama_70b/llama2_fq_0_int_4_-1_bs{batch_size}_seq{seq_len}_ci_False_async'
    else:
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/bloom_176b/llama2_fq_0_int_4_-1_bs{batch_size}_seq{seq_len}_ci_False_async'
    target_process = subprocess.Popen(f'cd {pwd}/ladder-benchmark; python {run_file} --prebuilt_path {model_file} ; cd ..', shell=True)
    return target_process

def ladder_fp16_nf4_inference(model='llama', batch_size=1, seq_len=1):
    run_file = 'ladder_with_fake_dense_dequantize.py'
    if model=='llama':
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/llama_70b/llama2_fq_0_nf_4_-1_bs{batch_size}_seq{seq_len}_ci_False_async'
    else:
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/bloom_176b/llama2_fq_0_nf_4_-1_bs{batch_size}_seq{seq_len}_ci_False_async'
    target_process = subprocess.Popen(f'cd {pwd}/ladder-benchmark; python {run_file} --prebuilt_path {model_file} ; cd ..', shell=True)
    return target_process

def ladder_fp8_fp8_inference(model='llama', batch_size=1, seq_len=1):
    run_file = 'ladder_with_fake_dense_dequantize.py'
    if model=='llama':
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/llama_70b/llama2_fq_0_fp_e5m2_8_-1_bs{batch_size}_seq{seq_len}_ci_False_async'
    else:
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/bloom_176b/llama2_fq_0_fp_e5m2_8_-1_bs{batch_size}_seq{seq_len}_ci_False_async'
    target_process = subprocess.Popen(f'cd {pwd}/ladder-benchmark; python {run_file} --prebuilt_path {model_file} ; cd ..', shell=True)
    return target_process

def ladder_fp16_mxfp8xmxfp8_inference(model='llama', batch_size=1, seq_len=1):
    run_file = 'ladder_with_fake_dense_dequantize.py'
    if model=='llama':
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/llama_70b/llama2_fq_0_mxfp_8_8_-1_bs{batch_size}_seq{seq_len}_ci_False_async'
    else:
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/bloom_176b/llama2_fq_0_mxfp_8_8_-1_bs{batch_size}_seq{seq_len}_ci_False_async'
    target_process = subprocess.Popen(f'cd {pwd}/ladder-benchmark; python {run_file} --prebuilt_path {model_file} ; cd ..', shell=True)
    return target_process

def ladder_fp16_int8xint1_inference(model='llama', batch_size=1, seq_len=1):
    run_file = 'ladder_with_fake_dense_dequantize.py'
    if model=='llama':
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/llama_70b/llama2_fq_0_int_1_-1_bs{batch_size}_seq{seq_len}_ci_True_async''
    else:
        model_file = f'{CHECKPOINT_PATH}/ladder/checkpoints/bloom_176b/llama2_fq_0_int_1_-1_bs{batch_size}_seq{seq_len}_ci_True_async'
    target_process = subprocess.Popen(f'cd {pwd}/ladder-benchmark; python {run_file} --prebuilt_path {model_file} ; cd ..', shell=True)
    return target_process

model_inference_mapping = {
    'pytorch': pytorch_inference,
    'onnxruntime': onnxruntime_inference,
    'tensorrt': tensorrt_inference,
    'vllm': vllm_inference,
    'vllm_fp16_int4': vllm_fp16_int4_inference,
    'welder': welder_inference,
    'ladder': ladder_inference,
    'ladder_fp16_int4': ladder_fp16_int4_inference,
    'ladder_fp16_nf4': ladder_fp16_nf4_inference,
    'ladder_fp8_fp8': ladder_fp8_fp8_inference,
    'ladder_fp16_mxfp8xmxfp8': ladder_fp16_mxfp8xmxfp8_inference,
    'ladder_fp16_int8xint1': ladder_fp16_int8xint1_inference
}

@contextlib.contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(previous_dir)

data = {}
path = './logs/{}_{}_{}_{}'.format(model, framework, batch_size, seq_len)
# create the directory if not exists
if not os.path.exists(path):
    os.makedirs(path)

memory_usage = 0
if os.path.exists(path):
    with pushd(path):
        print('Measure the memory for {} batch {} seq {} under {}'.format(model, batch_size, seq_len, framework))
        if os.path.exists('prepare_mem.sh'):
            os.system('bash prepare_mem.sh')
        # here start the inference process at the same time and
        # measure the memory at the same time
        inference_func = model_inference_mapping[framework]
        target_process = inference_func(model, batch_size, seq_len)
    sleep(7) # wait the memory to be steady
    monitor_process = subprocess.Popen('bash nvidia_measure_memory.sh > run.log', shell=True)
    try:
        target_process.wait(timeout=10)
    except Exception as err:
        try:
            target_process.terminate()
            time.sleep(10)
        except Exception as err:
            print(err)
    monitor_process.terminate()
    memory_usage = analyze_log('run.log')
data['{}_{}_{}_{}'.format(model, framework, batch_size, seq_len)] = memory_usage
print(data)
with open(f'{args.model}_data.json', 'w') as f:
    json.dump(data, f)