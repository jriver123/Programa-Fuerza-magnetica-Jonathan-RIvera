def producto_cruz(vec_a, vec_b, nombre_a="a", nombre_b="b"):
    """
    Calcula el producto cruz implementando la fórmula explícita del determinante.
    """
    i_comp = (vec_a[1] * vec_b[2]) - (vec_a[2] * vec_b[1])
    j_interna = (vec_a[0] * vec_b[2]) - (vec_a[2] * vec_b[0])
    j_comp = -j_interna
    k_comp = (vec_a[0] * vec_b[1]) - (vec_a[1] * vec_b[0])
    
    resultado = [i_comp, j_comp, k_comp]
    
    # Hemos dividido la fórmula en varias líneas para que no desborde horizontalmente
    proc = (
        f"   Fórmula:\n"
        f"   = ({nombre_a}2*{nombre_b}3 - {nombre_a}3*{nombre_b}2)i\n"
        f"     - ({nombre_a}1*{nombre_b}3 - {nombre_a}3*{nombre_b}1)j\n"
        f"     + ({nombre_a}1*{nombre_b}2 - {nombre_a}2*{nombre_b}1)k\n\n"
        f"   i = ({vec_a[1]:.1f} * {vec_b[2]:.1f}) - ({vec_a[2]:.1f} * {vec_b[1]:.1f}) = {i_comp:.2f}\n"
        f"   j = -( ({vec_a[0]:.1f} * {vec_b[2]:.1f}) - ({vec_a[2]:.1f} * {vec_b[0]:.1f}) ) = {j_comp:.2f}\n"
        f"   k = ({vec_a[0]:.1f} * {vec_b[1]:.1f}) - ({vec_a[1]:.1f} * {vec_b[0]:.1f}) = {k_comp:.2f}\n\n"
        f"   {nombre_a} x {nombre_b} = <{resultado[0]:.2f}, {resultado[1]:.2f}, {resultado[2]:.2f}>"
    )
    return resultado, proc

def calcular_fuerza_carga(q_microcoulombs, v_vector, b_vector):
    q_coulombs = q_microcoulombs * 1e-6
    v_cruz_b, proc_cruz = producto_cruz(v_vector, b_vector, "v", "B")
    fuerza = [q_coulombs * comp for comp in v_cruz_b]
    
    proc = (
        f"--- PROCEDIMIENTO ---\n"
        f"1. Convertir carga a Coulombs:\n"
        f"   q = {q_microcoulombs} µC  -->  {q_microcoulombs} x 10^-6 C\n\n"
        f"2. Calcular el producto cruz (v x B):\n"
        f"   v = <{v_vector[0]}, {v_vector[1]}, {v_vector[2]}>\n"
        f"   B = <{b_vector[0]}, {b_vector[1]}, {b_vector[2]}>\n\n"
        f"{proc_cruz}\n\n"
        f"3. Multiplicar por la carga q (F = q(v x B)):\n"
        f"   F = ({q_microcoulombs} x 10^-6) * <{v_cruz_b[0]:.2f}, {v_cruz_b[1]:.2f}, {v_cruz_b[2]:.2f}>\n"
        f"   F = <{fuerza[0]:.4f}, {fuerza[1]:.4f}, {fuerza[2]:.4f}> N"
    )
    
    return fuerza, proc

def calcular_fuerza_conductor(punto_p, punto_q, corriente_i, b_vector):
    vector_l = [
        punto_q[0] - punto_p[0],
        punto_q[1] - punto_p[1],
        punto_q[2] - punto_p[2]
    ]
    
    l_cruz_b, proc_cruz = producto_cruz(vector_l, b_vector, "L", "B")
    fuerza = [corriente_i * comp for comp in l_cruz_b]
    
    proc = (
        f"--- PROCEDIMIENTO ---\n"
        f"1. Calcular el vector L (Q - P):\n"
        f"   P = ({punto_p[0]}, {punto_p[1]}, {punto_p[2]})\n"
        f"   Q = ({punto_q[0]}, {punto_q[1]}, {punto_q[2]})\n"
        f"   L = <{vector_l[0]}, {vector_l[1]}, {vector_l[2]}>\n\n"
        f"2. Calcular el producto cruz (L x B):\n"
        f"   B = <{b_vector[0]}, {b_vector[1]}, {b_vector[2]}>\n\n"
        f"{proc_cruz}\n\n"
        f"3. Multiplicar por la corriente I (F = I(L x B)):\n"
        f"   I = {corriente_i} A\n"
        f"   F = {corriente_i} * <{l_cruz_b[0]:.2f}, {l_cruz_b[1]:.2f}, {l_cruz_b[2]:.2f}>\n"
        f"   F = <{fuerza[0]:.2f}, {fuerza[1]:.2f}, {fuerza[2]:.2f}> N"
    )
    
    return fuerza, proc