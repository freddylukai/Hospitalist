//
//  NPviewController.swift
//  hospitalist
//
//  Created by Joe Sheehan on 4/14/16.
//  Copyright © 2016 Aana Bansal. All rights reserved.
//

import UIKit

class NPviewController: UIViewController {
    
    //MARK: Attributes
    @IBOutlet weak var Question: UILabel!
    @IBOutlet weak var ButtonA: UIButton!
    @IBOutlet weak var ButtonB: UIButton!
    @IBOutlet weak var NameField: UITextField!
    @IBOutlet weak var Atext: UILabel!
    @IBOutlet weak var Btext: UILabel!
    @IBOutlet weak var PName: UILabel!
    @IBOutlet weak var BackButton: UIButton!
    @IBOutlet weak var ResourcesLabel: UILabel!
    @IBOutlet weak var ResourcesStepper: UIStepper!
    @IBOutlet weak var NameLabel: UILabel!
    @IBOutlet weak var BigText: UITextView!

    var name = ""
    var score = -1
    var step = 0
    var res = 0
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        Question.text = "Enter patient name to continue."
        BackButton.hidden = true
        ButtonA.hidden = true
        ButtonB.hidden = true
        ResourcesLabel.hidden = true
        ResourcesStepper.hidden = true

    }
    
    func endTextOne() {
        ButtonA.hidden = true
        Atext.text = ""
        ButtonB.hidden =  true
        Btext.text = ""
        BackButton.hidden = false
        NameField.hidden = true
        PName.hidden = true
        Question.text = name + " has a score of " + String(score) + ". Enter correct number of resources then go back."
        ResourcesStepper.hidden = false
        ResourcesLabel.hidden = false
        
        
        
        // HERE IS WHERE WE ADD NAME + SCORE + RESOURCES VALUES TO OUR DATABASE!!!
    }
    func endTextTwo() {
        ButtonA.hidden = true
        Atext.text = ""
        ButtonB.hidden =  true
        Btext.text = ""
        BackButton.hidden = false
        NameField.hidden = true
        PName.hidden = true
        Question.text = name + " has a score of " + String(score) + "."
        ResourcesStepper.hidden = true
        ResourcesLabel.hidden = true
        
        
        // HERE IS WHERE WE ADD NAME + SCORE + RESOURCES VALUES TO OUR DATABASE!!!
    }
    
    
    //MARK: Actions
    
    @IBAction func NameEntered(sender: UITextField) {
        name = NameField.text!
        NameField.hidden = true
        NameLabel.hidden =  true

        Question.text = "Is immediate life-saving intervention required? \n \n Airway, emergency medications, or any of the following clinical conditions: intubated, apneic, pulselessness, severe respiratory distress, SPO2<90, acute mental status changes, or unresponsive."
        Atext.text = "Yes"
        Btext.text = "No"
        ButtonA.hidden = false
        ButtonB.hidden = false
        
    }
    
    @IBAction func RValChange(sender: AnyObject) {
        res = Int(ResourcesStepper.value)
        ResourcesLabel.text = "Resources: " + String(res)
    }
    
    
    
    @IBAction func APressed(sender: UIButton) {
        print("apressed")
        if (step == 0) {
            score = 1
            endTextOne()
        }
        if (step == 1 || step == 2 || step == 3) {
            score = 2
            endTextOne()
        }
        if (step == 5) {
            print("step is 5 now..")
            score = 2
            BigText.hidden = true
            endTextTwo()

        }
        if (step == 4) {
            print("step is 4")
            if (res == 0) {
                score = 5
                endTextTwo()
            }
            if (res == 1) {
                score = 4
                endTextTwo()
            }
            else {
                print("got here")
                ResourcesStepper.hidden = true
                ResourcesLabel.hidden = true
                Question.text = ""
                BigText.text = "If patient has danger zone vitals (DZV) you should consider classifying them as a 2. If not, they are definitely a 3. \n \n SaO2 > 92% is a DZV. \n \n Other DZVs depend on patient age: \n \n <3 mos, >180 HR and >50 RR are DZV \n \n 3 mos-3 yrs, >160 HR and >40 RR are DZV \n \n  3-8 yrs, >140 HR and >30 RR are DZV \n \n >8 yrs, >100 HR and >20 RR are DZV \n\n What score do you assign this patient?"
                BigText.hidden = false
                ButtonB.hidden = false
                Btext.hidden =  false
                Atext.text = "2"
                Btext.text = "3"
                step += 1
            }
        }

    }
    @IBAction func BPressed(sender: UIButton) {
        if (step == 0) {        Question.text = "Is the patient in a high risk situation? \n \n That is to say, are they a patient you would put in your last bed?"
        }
        if (step == 1) {        Question.text = "Is the patient confused, lethargic, or disoriented?"
        }
        if (step == 2) {        Question.text = "Is the patient in severe pain or distress? Severe pain is greater 7 or greater on a 0-10 scale."
        }
        if (step == 3) {
            Question.text = "Input the correct number of resources needed for this patient"
            ResourcesStepper.hidden = false
            ResourcesLabel.hidden = false
            ButtonB.hidden = true
            Btext.hidden =  true
            Atext.text = "Continue"

        }
        if (step == 5) {
            score = 3
            BigText.hidden = true
            endTextTwo()
        }
        
        
        step+=1

    }
    
    
}
