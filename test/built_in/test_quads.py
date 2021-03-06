from helpers import compute_volume

import pygmsh


def test():
    with pygmsh.geo.Geometry() as geom:
        rectangle = geom.add_rectangle(0.0, 1.0, 0.0, 1.0, 0.0, 0.1)
        geom.set_recombined_surfaces([rectangle.surface])
        mesh = geom.generate_mesh(dim=2)

    ref = 1.0
    assert abs(compute_volume(mesh) - ref) < 1.0e-2 * ref
    return mesh


if __name__ == "__main__":
    test().write("quads.vtu")
