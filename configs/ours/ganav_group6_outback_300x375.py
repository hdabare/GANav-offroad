_base_ = [
    '../_base_/models/ours_class_att.py', '../_base_/datasets/outback_group6.py',
    '../_base_/default_runtime.py'
]


optimizer = dict(type='SGD', lr=0.003, momentum=0.9, weight_decay=4e-5)
optimizer_config = dict()
# learning policy
# runtime settings
runner = dict(type='IterBasedRunner', max_iters=1000)
total_iters = 1000
checkpoint_config = dict(by_epoch=False, interval=1000)
evaluation = dict(interval=1000, metric='mIoU')

# optimizer
lr_config = dict(policy='poly', power=0.9, min_lr=1e-4, warmup='linear',
    warmup_iters=250,
    warmup_ratio=1e-6,
    by_epoch=False)

data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2)


