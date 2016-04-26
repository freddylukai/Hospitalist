//
//  ViewController.swift
//  hospitalist
//
//  Created by Aana Bansal on 4/3/16.
//  Copyright © 2016 Aana Bansal. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var label: UITextField!
    @IBOutlet weak var queueButton: UIButton!
    @IBOutlet weak var resourceStatusButton: UIButton!
    @IBOutlet weak var newPatientButton: UIButton!
    
    
    
   /* @IBAction func link(sender: AnyObject) {
        //UIApplication.sharedApplication().openURL(NSURL(string: "http://ec2-52-90-89-173.compute-1.amazonaws.com/")!)
        let URL = NSURL(string: "http://ec2-52-90-89-173.compute-1.amazonaws.com/gettest")
        
        do {
            let htmlSource = try String(contentsOfURL: URL!, encoding: NSUTF8StringEncoding)
            print(htmlSource)
        }
            
        catch let error as NSError{
            print ("ERROR: \(error)")
        }
        
        
    }*/
    
    @IBAction func queue(sender: UIButton) {
        
    }
    
    @IBAction func resourceStatAction(sender: AnyObject) {
        
    }
    
    @IBAction func new(sender: AnyObject) {
        
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
}

