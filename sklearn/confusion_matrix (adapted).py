#Adadpet from: https://medium.com/data-hackers/entendendo-o-que-%C3%A9-matriz-de-confus%C3%A3o-com-python-114e683ec509

#Confusion Matrix

import numpy as np

# 1 for pregnant and 0 for non pregnant
real_values    = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
predict_values = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]

def get_confusion_matrix(reals_array, predicted_array, labels):
    """
    Uma função que retorna a matriz de confusão para uma classificação binária
    
    Args:
        reals_array (list): lista de valores reais
        predicted_array (list): lista de valores preditos pelo modelos
        labels (list): lista de labels a serem avaliados.
            É importante que ela esteja presente, pois usaremos ela para entender
            quem é a classe positiva e quem é a classe negativa
    
    Returns:
        Um numpy.array, no formato:
            numpy.array([
                [ tp, fp ],
                [ fn, tn ]
            ])
    """
    # Só duas classes (classificação binária)
    if len(labels) > 2:
        return None

    # Os vetores tem que ter tamanahos iguais
    if len(reals_array) != len(predicted_array):
        return None
    
    # considerando a primeira classe como a positiva, e a segunda a negativa

    # Pega o 1, nesse caso Positivo
    true_class = labels[0] 
    #Pega o 0, nesse caso Negativo
    negative_class = labels[1]

    # Contadores de valores preditos corretamente
    tp = 0 #true positive
    tn = 0 #true negative
    
    # Contadores de valores preditos incorretamente
    fp = 0 #false positive
    fn = 0 #false negative
    
    #reals_array: vetor de valores (classes) reais
    #predicted_array: vetor de valores (classes) preditas
    
    for (indice, v_real) in enumerate(reals_array):
        
        #enumerate(reals_array): i0, v_real0, i1, v_real1...

        v_predito = predicted_array[indice]

        # se trata de um valor real da classe positiva?
        if v_real == true_class:

            # true positive: ACERTOU
            tp += 1 if v_predito == v_real else 0

            # false positive: ERROU
            fp += 1 if v_predito != v_real else 0
        
        else: 
            #bora brincar de escrever o código legível
            # e ajeitar esses condicionais?

            #true negative: ACERTOU
            if (v_predito == v_real):
              tn += 1
            else: 
              tn += 0  
          
            # false negative: ERROU
            if(v_predito != v_real):
              fn += 1
            else:
              fn += 0  
 
    return np.array([
        # valores ditos da classe positiva
        [ tp, fp ],
        # valores ditos da classe negativa
        [ fn, tn ]
    ])

print(get_confusion_matrix(reals_array=real_values, predicted_array=predict_values, labels=[1,0]))
# array([[3, 1], [2, 4]])