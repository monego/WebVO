/***************************************************************************
Programa que realiza o agrupamento de partículas de acordo com o raio de
percolação fornecido, usando o algoritmo Friends of Friends.
Ultima atualização 12/01/2009
Autor: Renata S. Rocha Ruiz
******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <time.h>

//---------------------------------------------------------------------------
int  *igru, N;
float  *x, *y, *z, *v1, *v2, *v3;
//---------------------------------------------------------------------------
//---------------------------------------------------------------------------
/********************* Lendo o arquivo de dados de entrada *****************/
//---------------------------------------------------------------------------
bool LeDados(char *filename){
  int m;
  float vx, vy, vz;
  FILE  *file;
  file = fopen(filename,"rt");

  //Número de partículas
  fscanf (file, "%d", &N);

  //********* alocando memória************//
  igru  = new int [N];  // índice do grupo
  x  = new float [N];  // posição x da partícula;
  y  = new float [N];  // posição y da partícula;
  z  = new float [N];  // posição z da partícula
  v1 = new float [N];  // coordenada x da velocidade
  v2 = new float [N];  // coordenada y da velocidade
  v3 = new float [N];  // coordenada z da velocidade

  for (int i = 0 ; i < N ; i++){
    fscanf (file, "%d %f %f %f %f %f %f ", &m, &x[i], &y[i], &z[i], &v1[i], &v2[i], &v3[i]);
    igru[i] = 0;
  }

  fclose (file);
  return false;
}
//---------------------------------------------------------------------------
/**************************** Realiza o agrupamento ******************************/
//---------------------------------------------------------------------------

void Friends(float rperc){

  float dist;
  int i = 0;
  int k = 0;
  int j, l;

  for (i = 0; i < N; i++){
    //Identificador do grupo - Denomina um novo grupo
    if(igru[i] == 0){
      k++;
      igru[i] = k; //Encontra uma partícula sem grupo e começa um grupo para ela
      for (j = i ; j < N ; j++){ //Verifica os indices de igru a partir da partícula sem grupos
        if(igru[j] == k){ //Verifica se é um grupo ainda não definido
          for (l = (i + 1) ; l < N ; l++){ //Então percorre o resto do vetor de grupos
            if (igru[l] == 0){ //Se o grupo na posição l ainda não foi definido:
              //Calcula a distância entre a partícula atual(l) e a anterior(j)
              dist = (x[j] - x[l])*(x[j] - x[l]) + (y[j] - y[l])*(y[j] - y[l]) + (z[j] - z[l])*(z[j] - z[l]);
              if (dist <= (rperc*rperc)) //Se encontrou partículas amigas seta o grupo para k
                igru[l] = k;
            }
          }
        }
      }
    }
  }

/********************escrevendo arquivo de saida ************************/

  char str1[10],str2[10], str3[10];

  FILE *file;
  time_t timestamp;
  char resultado;
  sprintf(str2, "%.2lf", rperc);
  sprintf(str3, "%ld", time(&timestamp));

  strcpy(str1, "Grupos_RP");
  strcat(str1, str2);
  strcat(str1, "_");
  strcat(str1, str3);

  file = fopen(str1,"w");

  fprintf(file, "totalparticles:%d\tgroups:%d\n", N, k);

  for (i = 0 ; i < N ; i++)
    fprintf(file,"%4d %4d % 10.6e % 10.6e % 10.6e % 10.6e % 10.6e % 10.6e \n", i+1, igru[i], x[i], y[i],z[i],
  v1[i], v2[i],v3[i]);

  fclose (file);


  /********* Calculando a quantidade de particulas por grupo ************/
  int nn, si, mult;
  int *Ngr;

  Ngr  = new int [k+1];

    for ( nn = 1; nn <= k; nn++ ){ //Para todos os grupos
      mult = 0;
      for (si = 0; si < N; si++) //Para todas partículas
        if(igru[si] == nn) mult =  mult + 1; //Se a partícula pertence ao grupo analisado
          Ngr[nn] = mult; //Armazena número de partículas por grupo
    }

  int cont1 = 0;
  for (nn = 1 ; nn <= k ; nn++){
    printf("Grupo: %d Particulas: %d\n", nn, Ngr[nn]);
    if (Ngr[nn] > 1) cont1++;
  }
  printf("Grupos com massa maior que 1: %d \n", cont1);

  delete Ngr;

}

//---------------------------------------------------------------------------
/**************************** Limpa a memória ******************************/
//---------------------------------------------------------------------------
void LimpaMemoria(void){
  delete igru;
  delete x;
  delete y;
  delete z;
  delete v1;
  delete v2;
  delete v3;
}

//---------------------------------------------------------------------------
/***************************************************************************/
//---------------------------------------------------------------------------
main(int argc, char **argv){
  float  local_v[100], rperc;
  char *Arg1;

  /*if(argc != 3 ){
    puts( "Por favor entre com o nome do arquivo de dados e o raio de percolação!" );
    exit(1);
  }*/

  //Inicia o arquivo
  Arg1 = argv[1];
  rperc = atof(argv[2]);

  LeDados(Arg1);
  Friends(rperc);
  LimpaMemoria();

  return 0;
}
