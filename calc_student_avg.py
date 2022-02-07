import csv

#Read into the student_scores.csv file 
scores = open('student_scores.csv', 'r')

scores_file = csv.reader(scores, delimiter = ',')

#Open the student_avg.csv file to write into 
avg_outfile = open('student_avg.csv', 'w')

#Calculate the test score averages 
for score in scores_file:

    score1 = int(score[1])
    score2 = int(score[2])
    score3 = int(score[3])
    avg = (score1 + score2 + score3)/3 
    avg = (format(avg, ',.2f'))
    avg_outfile.write(score[0] + ',' + avg + '\n')

avg_outfile.close()