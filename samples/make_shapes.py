import trimesh

box = trimesh.creation.box(extents=(1, 1, 1))
ball = trimesh.creation.icosphere(subdivisions=3)
print('box   :', len(box.vertices), 'vertices,', len(box.faces), 'faces')
print('sphere:', len(ball.vertices), 'vertices,', len(ball.faces), 'faces')
box.export('samples/box.obj')
ball.export('samples/ball.glb')

print("\n--- BOX PROPERTIES ---")

print("Bounds:", box.bounds)
print("Watertight:", box.is_watertight)
print("Surface Area:", box.area)
print("Volume:", box.volume)


print("\n--- SPHERE PROPERTIES ---")

print("Bounds:", ball.bounds)
print("Watertight:", ball.is_watertight)
print("Surface Area:", ball.area)
print("Volume:", ball.volume)