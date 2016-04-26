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
    @IBOutlet weak var NameLabel: UILabel!
    @IBOutlet weak var BigText: UITextView!
    @IBOutlet weak var r1: UIButton!
    @IBOutlet weak var r2: UIButton!
    @IBOutlet weak var r3: UIButton!
    @IBOutlet weak var r4: UIButton!
    @IBOutlet weak var r5: UIButton!
    @IBOutlet weak var r6: UIButton!
    @IBOutlet weak var r7: UIButton!
    @IBOutlet weak var r8: UIButton!
    @IBOutlet weak var r9: UIButton!
    @IBOutlet weak var r10: UIButton!
    @IBOutlet weak var r11: UIButton!
    @IBOutlet weak var r12: UIButton!
    
    

    var name = ""
    var score = -1
    var step = 0
    var res = 0
    var resources = ["X-Ray","CT","MRI","Ultrasound","IV Fluids","IV Medication", "IM Medication", "Consultation", "Bed", "Doctor","Other", "ECG"]
    var theseResources = [0,0,0,0,0,0,0,0,0,0,0,0]

    
    func rHide() {
        r1.hidden = true
        r2.hidden = true
        r3.hidden = true
        r4.hidden = true
        r5.hidden = true
        r6.hidden = true
        r7.hidden = true
        r8.hidden = true
        r9.hidden = true
        r10.hidden = true
        r11.hidden = true
        r12.hidden = true
        Question.hidden = false
    }
    
    func rShow() {
        r1.backgroundColor = UIColor.lightGrayColor()
        r2.backgroundColor = UIColor.lightGrayColor()
        r3.backgroundColor = UIColor.lightGrayColor()
        r4.backgroundColor = UIColor.lightGrayColor()
        r5.backgroundColor = UIColor.lightGrayColor()
        r6.backgroundColor = UIColor.lightGrayColor()
        r7.backgroundColor = UIColor.lightGrayColor()
        r8.backgroundColor = UIColor.lightGrayColor()
        r9.backgroundColor = UIColor.lightGrayColor()
        r10.backgroundColor = UIColor.lightGrayColor()
        r11.backgroundColor = UIColor.lightGrayColor()
        r12.backgroundColor = UIColor.lightGrayColor()
        r1.hidden = false
        r2.hidden = false
        r3.hidden = false
        r4.hidden = false
        r5.hidden = false
        r6.hidden = false
        r7.hidden = false
        r8.hidden = false
        r9.hidden = false
        r10.hidden = false
        r11.hidden = false
        r12.hidden = false
        Question.hidden = true

    }
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        Question.text = "Enter patient name to continue."
        BackButton.hidden = true
        ButtonA.hidden = true
        ButtonB.hidden = true
        rHide()
        ResourcesLabel.hidden = true

    }
    
    func prepareString() -> String {
        let namesplit = name.componentsSeparatedByString(" ")
        var fname = ""
        if (namesplit.count > 0) {
            fname = namesplit[0]
        }
        var lname = ""
        if (namesplit.count > 1) {
            for i in 1...(namesplit.count - 1) {
                lname += namesplit[i]
            }
        }
        var outstr = "first_name="+fname+"&last_name="+lname+"&age=0&esi=" + String(score) + "&res="
        var first = 0
        for i in 0...(theseResources.count - 1) {
            if (theseResources[i] == 1) {
                if (first == 0) {
                    outstr += String(i)
                    first += 1
                }
                else {
                    outstr += ("," + String(i))
                }
            }
        }
        
        
        return outstr
    }
    
    func sendRequest() {
        let request = NSMutableURLRequest(URL: NSURL(string: "http://ec2-52-90-89-173.compute-1.amazonaws.com/newpatient/")!)
        request.HTTPMethod = "POST"
        let postString = prepareString()
        print("poststring is"+postString)
        request.HTTPBody = postString.dataUsingEncoding(NSUTF8StringEncoding)
        let task = NSURLSession.sharedSession().dataTaskWithRequest(request) { data, response, error in
            guard error == nil && data != nil else {                                                          // check for fundamental networking error
                print("error=\(error)")
                return
            }
            
            if let httpStatus = response as? NSHTTPURLResponse where httpStatus.statusCode != 200 {           // check for http errors
                print("statusCode should be 200, but is \(httpStatus.statusCode)")
                print("response = \(response)")
            }
            
            let responseString = NSString(data: data!, encoding: NSUTF8StringEncoding)
            print("responseString = \(responseString)")
        }
        task.resume()
    }
    
    
    @IBAction func BackButtonPunched(sender: UIButton) {
        sendRequest()
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
        rShow()
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
        rHide()
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
    
    func getRNum(resText: String) -> Int {
        for index in 0...13 {
            if (resText == resources[index]) {
                return index
            }
        }
        return 14
    }
    
    @IBAction func ResourceClicked(sender: UIButton) {
        if (sender.backgroundColor == UIColor.blueColor()) {
            sender.backgroundColor = UIColor.lightGrayColor()
            res -= 1
            let cur = sender.currentTitle!
            let index = getRNum(cur)
            theseResources[index] = 0
        }
        else {
            sender.backgroundColor = UIColor.blueColor()
            res += 1
            let cur = sender.currentTitle!
            let index = getRNum(cur)
            theseResources[index] = 1
        }
        
        ResourcesLabel.text = "Select necessary resources Selected: " + String(res)
        
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
                rHide()
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
            rShow()
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
