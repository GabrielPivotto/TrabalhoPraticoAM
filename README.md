# TrabalhoPraticoAM

Integrantes:  Gabriel Andreis Pivotto (23111870), 
              Giordano Fraga Faccioli (23201049), 
              Pedro Duarte dos Santos (23200087)

Algoritmos escolhidos para a tarefa A:
- HDBSCAN
- K-Prototypes

Algoritmos escolhidos para a tarefa B:
- PCA
- t-SNE

Antes de rodar QUALQUER notebook neste projeto, certifique-se que requirements foi feito. Digite ```pip install -r requirements.txt``` para baixar todas as dependências necessárias. Para reproduzir os resultados, basta executar os scripts na pasta ``scripts_pre_process`` (primeiro ``pre_processamento_baseline`` depois ``pre_processamento_kprototype``) e rodar os demais notebooks presentes
<br>
## Explicação dos arquivos:
- ``analise_inicial.ipynb``: engloba todo o processo de exploração dos dados para definir o que limpar.
- ``Modelo_K-Prototypes.ipynb`` e ``Modelo_HDBSCAN.ipynb``: demonstra o pré-processamento para treinamento dos modelos + gráficos de métricas e desempenho, além de mostrar a caracterização dos clusters.
- ``analise_B.ipynb``: engloba todo o processo de desenvolvimento para a tarefa B do trabalho.
- ``scripts_pre_process``: pasta que guarda os scripts de pre-processamento
  - ``pre_processamento_baseline``: limpeza base dos dados (imputação de nulos, padronização de dados etc.)
  - ``pre_processamento_kprototype``: limpeza especifica ao modelo K-Prototype
