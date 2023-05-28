import matplotlib.pyplot as plt

def scatter_graph(combo, score, time_list, model_name):
    """
    This function plots accuracy for each varation for a given model 
    """

    x1 = []
    x2 = []
    x3 = []

    y1 = []
    y2 = []
    y3 = []

    for i, v in enumerate(combo):   
        if v[1] == "unigram":
            y1.append(score[i])
            x1.append(time_list[i])
        if v[1] == "bigram":
            y2.append(score[i])
            x2.append(time_list[i])
        if v[1] == "trigram":
            y3.append(score[i])
            x3.append(time_list[i])
    
    fig, ax = plt.subplots()
    
    #resizing window 
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('test2png.png', dpi=100)

    # depict illustration
    ax.scatter(x1, y1)
    ax.scatter(x2, y2)
    ax.scatter(x3, y3)
 
    # apply legend()
    ax.legend(["unigram" , "bigram", "trigram"])

    #labels 
    ax.set_ylabel('Accuracy')
    ax.set_xlabel('Run Time')
    ax.set_title(model_name + ' Accuracy Plot by Run Time')
    
    plt.show()


def graph_score(combo, score, model_name):
    """
    This function plots accuracy and f1 scores for each varation for a given model 

    """
    #changing data type 
    x = [str(label) for label in combo]
    y = [float(value) for value in score]

    fig, ax = plt.subplots()

    #resizing window 
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('test2png.png', dpi=100)

    ax.bar(x, y)

    ax.set_xticks(range(len(combo)))
    ax.set_xticklabels(x, rotation=-45, ha="left")

    #labels 
    ax.set_ylabel('Accuracy and F1 Score')
    ax.set_title(model_name + ' Accuracy Plot for Hyperparameter Tuning')

    plt.show()

def graph_time(combo, time_lst, model_name):
    """
    This function plots accuracy for each varation for a given model 

    """
    #changing data type 
    x = [str(label) for label in combo]
    y = [float(value) for value in time_lst]

    fig, ax = plt.subplots()

    #resizing window 
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('test2png.png', dpi=100)

    ax.bar(x, y)

    ax.set_xticks(range(len(combo)))
    ax.set_xticklabels(x, rotation=-45, ha="left")

    #labels 
    ax.set_ylabel('Runtime')
    ax.set_title(model_name + ' Model Run Time For Hyperparameter Tuning')

    plt.show()