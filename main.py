import mass as ms


def run_circle():
    earth = ms.Body(10, 10, [0, 0], [0, 0])
    mars = ms.Body(10, 10, [10.0, 0.0], [0.0, 10.0])

    e_pos = []
    m_pos = []

    dt = 0.001
    for i in range(7000):
        force_mag = ms.get_gravity(earth, mars)
        unit_dir = earth.get_direction(mars)

        f_g = -force_mag*unit_dir
        mars.apply_force(f_g, dt)

        e_pos.append(earth.get_pos())
        m_pos.append(mars.get_pos())

    return m_pos


def run():
    earth = ms.Body(1000, 10, [0, 0], [0, 0])
    mars = ms.Body(10, 10, [10.0, 0.0], [0.0, 10.0])

    e_pos = []
    m_pos = []

    dt = 0.001
    for i in range(7000):
        force_mag = ms.get_gravity(earth, mars)
        unit_dir = earth.get_direction(mars)

        f_g = -force_mag * unit_dir
        mars.apply_force(f_g, dt)
        earth.apply_force(-1*f_g, dt)

        e_pos.append(earth.get_pos())
        m_pos.append(mars.get_pos())

    return e_pos, m_pos
