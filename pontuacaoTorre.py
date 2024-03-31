import pandas as pd


# Definição corrigida da função fora do loop
def calculate_score(nome, idade, acertos):

    scores_dict = {
        11: [0,0,0,0,0,0,0,0,3,8,13,18,24,29,34,39,44,50,55,60,65,70,76,81,86,91,96,102,107,112,117,122,128,133,138,143],
        12: [0,0,0,0,0,0,0,0,0,0,0,0,4,10,16,22,28,34,40,46,51,57,63,69,75,81,87,93,99,105,111,116,122,128,134,140],
        13: [0,0,0,0,0,0,0,0,1,6,11,15,20,25,29,34,39,43,48,53,58,62,67,72,76,81,86,90,95,100,104,109,114,118,123,128],
        14: [0,0,0,0,4,8,12,16,20,24,27,31,35,39,43,47,50,54,58,62,66,70,74,77,81,85,89,93,97,100,104,108,112,116,120,123]
        }

        # Converting dictionary to DataFrame for easy look-up
    scores_df = pd.DataFrame(scores_dict)

    idade = int(idade)
    acertos = int(acertos)
    if idade in scores_df.columns:
        standardized_score = scores_df[idade][acertos - 1] if acertos - 1 < len(scores_df[idade]) else 'NA'
        if standardized_score == 'NA':
            classification = 'Acertos fora do alcance'
        elif standardized_score < 70:
            classification = 'Muito baixa'
        elif 70 <= standardized_score < 85:
            classification = 'Baixa'
        elif 85 <= standardized_score < 115:
            classification = 'Média'
        elif 115 <= standardized_score < 130:
            classification = 'Alta'
        else:
            classification = 'Muito alta'
    else:
        standardized_score = 'NA'
        classification = 'Idade fora do alcance'
    
    print("---------------------------")
    print(f"Pontuação: {standardized_score}")
    print(f"Classificação: {classification}")

    return {
        'student_name': nome,
        'age': idade,
        'raw_score': acertos,
        'standardized_score': standardized_score,
        'classification': classification
    }
