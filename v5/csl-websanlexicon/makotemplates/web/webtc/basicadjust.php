<?php
error_reporting(E_ALL & ~E_NOTICE & ~E_WARNING);
?>
<?php 
/*basicadjust.php
BasicAdjust class  Takes a parameter object
   and a list of xml records from the dictionary database,
   and adjust each of these records so it is ready for the BasicDisplay.
   This was formerly done by the BasicDisplay class in line_adjust function.
   The hope is to have dictionary specific code in this BasicAdjust class,
   and to have the BasicDisplay class to be identical for all dictionaries.
03-16-2023  Simplified to work under 'kosha-dev'
*/
require_once('dal.php');
require_once('dbgprint.php');
class BasicAdjust {
 public $getParms;
 public $adjxmlrecs;
 public $dal_ab, $dal_auth; // 
 public $accent;
 public $dbg;
 public $pagecol;
 public $dict, $key;
 public function __construct($getParms,$xmlrecs) {
  $this->accent = $getParms->accent;
  $dict = $getParms->dict;
  $this->dict = $dict;
  $key = $getParms->key;
  $this->key = $key;
  $this->dbg=false;
  $this->dal_ab = new Dal($dict,"ab");
  if (in_array($dict,array('xxx'))){
   // $this->dal_auth = new Dal($dict,"authtooltips");
  }else {
   $this->dal_auth = null;
  }
 
  $this->getParms = $getParms;
  $this->adjxmlrecs = array();
  $i = 0;
  foreach($xmlrecs as $line) {
   $this->pagecol = '';
   $line1 = $this->line_adjust($line);
   $this->adjxmlrecs[] = $line1;
   $i = $i + 1;
   dbgprint($this->dbg,"basicadjust: i=$i line=\n$line\n\nadjline=$line1\n");
  }
  
 }
 public function line_adjust($line) {
 $dbg = false;
 $line = preg_replace('|<hwdetails>(.*?)</hwdetails>|',
         '<div style="background-color: beige;">\1</div>',$line);
  // for koshas like anhk, abch
  $line = preg_replace_callback('|<hwdetail><hw>(.*?)</hw><meaning>(.*?)</meaning></hwdetail>|',
    'BasicAdjust::meaning_callback',
     $line);
     
  // for koshas like abch
  $line = preg_replace_callback('|<hwdetail><eid>(.*?)</eid><syns>(.*?)</syns></hwdetail>|',
    'BasicAdjust::syns_callback',
     $line);
  
 $line = preg_replace('|<entrydetails>(.*?)</entrydetails>|',
   '<lb/>\1',$line);
 $line = preg_replace('|<entrydetail>(.*?)</entrydetail>|',
           '<div>\1</div>',$line);
 return $line;
}
public function meaning_callback($matches) {
 // OLD: <hwdetail>naga-pum</hw><meaning>sarpa,gaja,sirsa</meaning><hwdetail>
 // NEW: <div><b>naga-pum</b> meaning(s) sarpa, gaja, sirsa</div>
 $hw = $matches[1];
 $meanings = $matches[2];  // a,b,c
 $meanings1 = str_replace(',', ', ',$meanings);
 $ans = "<div><b>$hw</b> meaning(s) $meanings1</div>";
 return $ans;
}
public function syns_callback($matches) {
 // OLD: <hwdetail><eid>A</eid><syns>B</syns></hwdetail>
 // NEW: 
 $eid = $matches[1]; 
 $synstr = $matches[2];
 if (! (preg_match('|^<s>(.*?)</s>$|',$synstr,$tempmatch))) {
  // should not occur
  $synstr1 = str_replace(',', ', ',$synstr);
  $ans = "<div> syngroup $eid:  $synstr1</div>";
  return $ans;
 }

 $key = $this->key;
 $synstr1 = $tempmatch[1];
 $items = preg_split('| *, *|',$synstr1);
 $syns = [];
 $html = "";
 $j = 0;
 $nitems = count($items);
 $i = 1;
 $prevgen = null;
 foreach($items as $item) {
  if ($j == 5) {
   $html = $html . "<br/>";
   $j = 0;
  }
  list($syn,$gen) = preg_split('|-|',$item);
  $syn1 = "<s>$syn</s>";
  if ($syn == $key) {
   // emphasize the display for the user request
   //$syn1 = "EMPHASIZE ($key) <span style='color:red'>$syn1</span>";
   $syn1 = "<span style='font-size:larger;'>$syn1</span>";
  }
  if ($gen == $prevgen) {
   $html = $html . "$syn1";
  } else {
   // different gender than previous. Show gender
   $html = $html . "$syn1-<s>$gen</s>";
  }
  $prevgen = $gen;
  if ($i != $nitems) {
   $html = $html . ", ";
  }
  $i = $i + 1;
  $j = $j + 1;
 }
 $ans = "syngroup $eid:<br/>$html";
 //dbgprint(true,"basicadjust syn callback html=\n  $html\n");
 return $ans;
}

public function syns_callback_v1($matches) {
 // OLD: <hwdetail><eid>A</eid><syns>B</syns></hwdetail>
 // NEW: 
 $eid = $matches[1]; 
 $synstr = $matches[2];
 if (! (preg_match('|^<s>(.*?)</s>$|',$synstr,$tempmatch))) {
  $synstr1 = str_replace(',', ', ',$synstr);
  $ans = "<div> syngroup $eid:  $synstr1</div>";
  return $ans;
 }

 $synstr1 = $tempmatch[1];
 $items = preg_split('| *, *|',$synstr1);
 $syns = [];
 $html = "<table>";
 $i = 0;
 $html = $html . "<tr>";
 foreach($items as $item) {
  if ($i == 5) {
   $html = $html . "</tr>";
   $html = $html . "<tr>";
   $i = 0;
  }
  list($syn,$gen) = preg_split('|-|',$item);
  $html = $html . "<td><s>$syn</s></td>";
  $i = $i + 1;
 }
 $html = $html . "</tr>";  // not always right!
 $html = $html . "</table>";
 
 $ans = "syngroup $eid:<br/>$html";
 //dbgprint(true,"basicadjust syn callback html=\n  $html\n");
 return $ans;
}

public function syns_callback_v0($matches) {
 // OLD: <hwdetail><eid>A</eid><syns>B</syns></hwdetail>
 // NEW: 
 $eid = $matches[1]; 
 $syns = $matches[2];  
 $syns1 = str_replace(',', ', ',$syns);
 $ans = "<div> syngroup $eid:  $syns1</div>";
 return $ans;
}

}

?>
