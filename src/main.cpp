/**
 * @note Base para o QT
 */

#include <iostream>
#include <fstream>

//===================================================
//  VARS
//===================================================

//===================================================
// FUNCOES
//===================================================

//  @brief Calculo para retornar o valor da
//  capacidade de carga dinamica (C)
//
//  @param fh Coeficiente de Vida (adimensional)
//  @param fn Coeficiente de Rotacao (adimensional)
//  @param P Carga Dinamica Equivalente (kN)
//
//  @return Capacidade de Carga Dinamica (kN)
float capacidade_de_carga_dinamica(float fh, float fn, float P)
{
    return (fh / fn);
}

//  @brief Calculo para retornar o valor da
//  Carga Dinamica equivalente (P)
//
//  @param x Fator Radial (adimensional)
//  @param y Fator Axial (adimensional)
//  @param Fr Carga Radial (kN)
//  @param Fa Carga Axial (kN)
float carga_dinamica_equivalente(float x, float y, float Fr, float Fa)
{
    return (x * Fr + y * Fa);
}

//===================================================
//  MAIN
//===================================================
int main(int argc, char **argv)
{

    return 0;
}