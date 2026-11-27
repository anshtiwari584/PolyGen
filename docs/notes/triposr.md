# Day 2 - TripoSR Smoke Test

## Objective
Generate a 3D mesh from a 2D image using TripoSR.

## Environment
- Platform: Google Colab
- GPU: NVIDIA Tesla T4
- Python: 3.13.16
- PyTorch: 2.14.1+cu130
- CUDA: 13.0

## Input
- Image: examples/chair.png

## Output
- Generated file: mesh.obj
- File size: approximately 4443 KB
- Output directory: outputs/triposr_test/

## Performance
- Model initialization: 13.00482 seconds
- Image processing: 3.56691 seconds
- Model inference: 5.29783 seconds
- Mesh extraction: 2.58979 seconds
- Export: 0.25193 seconds
- Sum of logged stages: 24.71 seconds

## Mesh Information
- Vertices: 42152
- Triangles: 84158
- Watertight: False
- Surface Area: 1.4883367253105493
- Volume: 0.06451613802315123

## GPU Memory
- GPU: NVIDIA Tesla T4
- Memory usage: 15360MiB

## Learning
- Successfully generated a 3D mesh from an image.
- Learned how TripoSR performs image-to-3D reconstruction.
- Learned how to inspect generated meshes using Trimesh and Blender.

## Done
- GPU environment configured.
- TripoSR installed.
- Chair image processed.
- 3D mesh generated.

## Broke
- Faced dependency installation issues.
- Resolved torchmcubes build issue.
- Resolved missing dependencies and Python compatibility issues.

## Tomorrow
- Create our own reusable image_to_mesh() function.