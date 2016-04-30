//
//  PatientTableViewController.swift
//  hospitalist
//
//  Created by Aana Bansal on 4/18/16.
//  Copyright © 2016 Aana Bansal. All rights reserved.
//

import UIKit
import Freddy

class PatientTableViewController: UITableViewController {

    // MARK: Properties
    
    var patients = [Patient]()
    
    override func viewDidLoad() {
        super.viewDidLoad()

        //load the sample data.
        //loadSamplePatients()
        
        //read from database
        loadPatients()
    }

    /*func loadSamplePatients(){
        let patient1 = Patient(name: "Doug Stamper", index: 1)
        let patient2 = Patient(name: "Zoe Barnes", index: 4)
        let patient3 = Patient(name: "Frank Underwood", index: 3)
        
        patients.append(patient1!)
        patients.append(patient2!)
        patients.append(patient3!)
    }*/
    
    
    
    func loadPatients(){
        let URL = NSURL(string: "http://ec2-52-90-89-173.compute-1.amazonaws.com/queue/")
        
        do {
            print("here we are")
            
            var optData:NSData? = nil
            do {
                optData = try NSData(contentsOfURL: URL!, options: NSDataReadingOptions())
            }
            catch {
                print("Handle \(error) here")
            }
            print("what about here")
            if let data = optData {
                print("here i am")
                let myj = try JSON(data: data)
                print("did we get this far")
                print(myj)
                let jres = try myj.array("patients")
                for (index, v) in jres.enumerate() {
                    print("index = " + String(index))
                    print("v = " + String(v))
                    let fnam = try v.string("firstname")
                    print("fname : "+fnam)
                    let lnam = try v.string("lastname")
                    print("lname : "+lnam)
                    let full = fnam + " " + lnam
                    let tot = Int(try v.string("esi"))
                    print("tot : "+String(tot))
                    let ava = Int(try v.string("ID"))
                    print("ava : "+String(ava))
                    
                    let cur = Patient(name: full, index: tot!, id: ava!)
                    patients.append(cur!)
                }
            }
        }
            
        catch let error as NSError{
            print ("ERROR: \(error)")
        }
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        
        return 1
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {

        return patients.count
    }

    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        // Table view cells are reused and should be dequeued using a cell identifier.
        let cellIdentifier = "PatientTableViewCell"
        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentifier, forIndexPath: indexPath) as! PatientTableViewCell
        
        // Fetches the appropriate meal for the data source layout.
        let patient = patients[indexPath.row]
        
        cell.nameLabel.text = patient.name
        cell.indexLabel.text = "ESI: " + String(patient.index)
        cell.id = patient.id
        
        return cell
    }
}
