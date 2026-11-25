# Devlog

## Day 0
- Done: created the polygen repo on GitHub, cloned it into VS Code, created the folder structure, set up the Python virtual environment (.venv), installed fastapi, trimesh, numpy, pillow and scipy.
- Broke: nothing
- Learned: what a virtual environment is, and what a .gitignore file does.
- Tomorrow: Day 1, create my first 3D mesh with trimesh and look at the OBJ file.

## Day 1 - Basic Mesh Creation

### Tasks Completed
- Created the basic project structure.
- Created make_shapes.py using Trimesh.
- Generated box.obj.
- Generated ball.glb.

### Mesh Observations

#### Box
- Vertices: 8
- Faces: 12
- Each vertex contains X, Y, Z coordinates.
- The cube consists of 6 square sides.
- Each square side is represented by 2 triangles.

#### Sphere
- Vertices: 642
- Faces: 1280
- Created using icosphere with subdivisions=3.
- The sphere is represented by triangular faces.

### Trimesh Properties
- bounds: Minimum and maximum mesh coordinates.
- is_watertight: Checks whether the mesh is closed.
- area: Calculates total surface area.
- volume: Calculates enclosed volume.

### Learning
Understood the basic concepts of vertices, faces,
triangular meshes and 3D mesh properties.

### Completed
- Created box using Trimesh.
- Created sphere using Trimesh.
- Exported box as OBJ.
- Exported sphere as GLB.
- Viewed both models in Blender.
- Viewed sphere using online GLB viewer.

### Learning
- Understood vertices and faces.
- Learned how triangular meshes work.
- Understood OBJ and GLB file formats.
- Explored basic Trimesh mesh properties.