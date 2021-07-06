import pypcd
import numpy as np
import open3d

pc = pypcd.PointCloud.from_path('0.pcd')

cloud = [list(p) for p in pc.pc_data[:]]
cloud = np.array(cloud)
cloud = cloud[~np.isnan(cloud).any(axis=1), :]
pointcloud = open3d.geometry.PointCloud()
pointcloud.points = open3d.utility.Vector3dVector(cloud[:,:3])
intensity = cloud[:,3]
print("min:", np.min(intensity), "max:", np.max(intensity))
pointcloud.colors = open3d.utility.Vector3dVector(np.tile(intensity[:, np.newaxis],(1,3)))
vis = open3d.visualization.Visualizer()
vis.create_window(window_name="pcd")
vis.get_render_option().point_size = 1
opt = vis.get_render_option()
opt.background_color = np.asarray([0, 0, 0])
vis.add_geometry(pointcloud)
vis.run()
vis.destroy_window()
