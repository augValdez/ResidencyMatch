"""
ResidencyMatch.py

This algorithm operates by reading an input file of the form

[residents | hospitals] preference 1, preference 2, preference 3, preference 4, ...

Any whitespace occurring in the input files is stripped off.

Usage:

    python ResidencyMatch.py [residents preference file] [hospitals preference file]

[Bernard Kintzing, Augustine Valdez]

8/28/2019

"""

import sys
import csv


class ResidencyMatch:

    # behaves like a constructor
    def __init__(self):
        """
        Think of
        
            unmatchedHospitals
            residentsMappings
            hospitalsMappings
            matches
            
        as being instance data for your class.
        
        Whenever you want to refer to instance data, you must
        prepend it with 'self.<instance data>'
        """
        
        # list of unmatched hospitals
        self.unmatchedHospitals = [ ]

        # list of unmatched residents
        self.unmatchedResidents = [ ]
        
        # dictionaries representing preferences mappings

        self.residentsMappings = { }
        self.hospitalsMappings = { }
        
        # dictionary of matches where mapping is resident:hospital
        self.matches = { }
        
        # read in the preference files
        
        '''
        This constructs a dictionary mapping a resident to a list of hospitals in order of preference
        '''
        
        prefsReader = csv.reader(open(sys.argv[1], 'r'), delimiter=',')

        for row in prefsReader:
            resident = row[0].strip()

             # all hospitals are initially unmatched
            self.unmatchedResidents.append(resident)

            # maps a resident to a list of preferences
            self.residentsMappings[resident] = [x.strip() for x in row[1:]]
            
            # initially have each resident as unmatched
            self.matches[resident] = None
        
        '''
        This constructs a dictionary mapping a hospital to a list of residents in order of preference
        '''
        
        prefsReader = csv.reader(open(sys.argv[2], 'r'), delimiter=',')
        for row in prefsReader:
            
            hospital = row[0].strip()
            
            # all hospitals are initially unmatched
            self.unmatchedHospitals.append(hospital)
            
            # maps a resident to a list of preferences
            self.hospitalsMappings[hospital] = [x.strip() for x in row[1:]] 

    def reportMatches(self):
        print(self.matches)
            
    def runMatch(self):
        uH = self.unmatchedHospitals
        uR = self.unmatchedResidents
        rM = self.residentsMappings
        hM = self.hospitalsMappings
        matches = self.matches

        while uH:
            hospital = uH[0]
            #for resident in hospital prefs
            for resident in hM[hospital]:
                #if resididnt is in the unmatched resisdents
                if resident in uR:
                    #match the resident to that hospital
                    matches[resident] = hospital
                    #remove the resident
                    uR.pop(uR.index(resident))
                    #remove the hopsital
                    uH.pop(uH.index(hospital))
                    print(matches)
                    break
                else:
                    #if the resident IS matched check the residents preferences between
                    #the hospital that it is matched with already and the new one that wants it
                    if rM[resident].index(hospital) < rM[resident].index(matches[resident]):
                        # add the NOW unmatched hospital from matches at residents index to unmatched hosptials 
                        uH.append(matches[resident])
                        # add the new hospital match with the resident to matches
                        matches[resident] = hospital
                        # pop the hospital that now got matched
                        uH.pop(uH.index(hospital))
                        break


if __name__ == "__main__":
   
    # some error checking
    if len(sys.argv) != 3:
        print('ERROR: Usage\n python ResidencyMatch.py [residents preferences] [hospitals preferences]')
        quit()

    # create an instance of ResidencyMatch 
    match = ResidencyMatch()

    # now call the runMatch() function
    match.runMatch()
    
    # report the matches
    match.reportMatches()
