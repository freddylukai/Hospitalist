//
//  PatientTableViewController.swift
//  hospitalist
//
//  Created by Aana Bansal on 4/18/16.
//  Copyright © 2016 Aana Bansal. All rights reserved.
//

import UIKit

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

    func loadSamplePatients(){
        let patient1 = Patient(name: "Doug Stamper", index: 1)
        let patient2 = Patient(name: "Zoe Barnes", index: 4)
        let patient3 = Patient(name: "Frank Underwood", index: 3)
        
        patients.append(patient1!)
        patients.append(patient2!)
        patients.append(patient3!)
    }
    
    func loadPatients(){
        let URL = NSURL(string: "http://ec2-52-90-89-173.compute-1.amazonaws.com/gettests")
        
        do {
            let htmlSource = try NSString(contentsOfURL: URL!, encoding: NSUTF8StringEncoding)
            let data = htmlSource.dataUsingEncoding(NSUTF8StringEncoding, allowLossyConversion: false)!
            
            
            print(htmlSource)
            print(data)

            do {
                let json = try NSJSONSerialization.JSONObjectWithData(data, options: NSJSONReadingOptions.AllowFragments ) as! [String: AnyObject]
                
                if let p = json["patientnames"] as? [String] {
                    print(p)
                }
            } catch {
                print("error: \(error)")
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
        cell.indexLabel.text = String(patient.index)
        
        return cell
    }

    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
