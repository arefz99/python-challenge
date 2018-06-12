#hello this is main body - appear after func declaration
import os

# Module for reading CSV's
import csv


#----------Define function so you can use all the time
def process_bank_files(input_file,output_file):

    #initialize vars
    row_num = 0
    months = 0
    revenue = 0
    revenue_change = 0
    average_rev_change = 0
    current_rev = 0
    prior_row_revenue = 0
    #greatest increase and decrease in revenue
    GIIR = 0
    GDIR = 0
    # months during which we had the greatest increase and decrease in revenue
    GIIR_month = ""
    GDIR_month = ""

    with open(input_file, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        
        # Skip the first row of the csv
        next(csv_reader, None)
        
        # Loop through rows
        for row in csv_reader:
            #   this counts the number of months of data not the number of unique months
            months = months + 1
            
            # determine The total amount of revenue gained over the entire period
            revenue = revenue + float(row[1])
            
            #start with row num 1 cuz row 0 is titles and then increment each pass thru
            #there is probably a better way to determine # of rows and used that as an index
            row_num = row_num +1
            #first row is speciallllll
            if row_num == 1:
                #establish first row revenue values
                prior_row_revenue =  float(row[1])
                revenue_change = 0
            #Other rows are not :-)
            else:
                current_rev =float(row[1])
                delta = current_rev - prior_row_revenue
                revenue_change = revenue_change + delta
                # debugging statement ignore ===> print ("in loop", i, "current = ", current_rev, "Prior was: ", prior_row_revenue, "Delta is ", delta)
                # determine  The greatest increase and the greatest decrease in revenue (date and amount) over the entire period

                if delta > GIIR:
                    GIIR = delta
                    GIIR_month = str(row[0])
                if delta < GDIR:
                    GDIR = delta
                    GDIR_month = str(row[0])
                
                prior_row_revenue = current_rev
            #End of IF
        #End of with

    # out of all loops - print results
    print ("Financial Analysis")
    print ("----------------------------")
    print ("Total Months: ", months)
    print ("TOTAL Revenue: ", '${:.0f}'.format(revenue))
    # determine The average change in revenue between months over the entire period
    average_rev_change = revenue_change / row_num

    print ("Average Revenue Change: ", '${:.0f}'.format(average_rev_change))
    print ("Greatest Increase in Revenue: ", GIIR_month, '${:.0f}'.format(GIIR))
    print ("Greatest Decrease in Revenue: ", GDIR_month, '${:.0f}'.format(GDIR))

    #write to file - one row per each CSV File results

    with open(output_file, 'w', newline='') as csvfile:
        
        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')
        
        # Write the first row (column headers)
        csvwriter.writerow(['Total Months', 'Total Revenue', 'Average Revenue Change', ' Greatest Increase in Revenue Month Occured', 'Greatest Increase in Revenue', ' Greatest Decrease in Revenue Month Occured', 'Greatest Decrease in Revenue'])
        
        # Write the second row
        csvwriter.writerow([months, revenue, average_rev_change, GIIR_month, GIIR, GDIR_month, GDIR])



#END FUNCTION CODE-----------------------------------------------------

#Mental DMZ :-)

#-------- THE MAIN PROGRAM---------------------
#setup files and paths
data1_csv_path = os.path.join('.', 'raw_data', 'budget_data_1.csv')
data2_csv_path = os.path.join('.', 'raw_data', 'budget_data_2.csv')
output1_path = os.path.join('financial_analysis_results1.csv')
output2_path = os.path.join('financial_analysis_results2.csv')

#feed files to function *chomp* *chomp*
process_bank_files(data1_csv_path, output1_path)
process_bank_files(data2_csv_path, output2_path)


