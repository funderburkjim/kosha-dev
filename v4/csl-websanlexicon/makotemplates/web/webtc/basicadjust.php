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
 public $dict;
 public function __construct($getParms,$xmlrecs) {
  $this->accent = $getParms->accent;
  $dict = $getParms->dict;
  $this->dict = $dict;
  $key = $getParms->key;
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
  // for koshas like anhk
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
 // OLD: <hwdetail>naga-pum</hw><meaning>sarpa,gaja,sirsa</meaning><hwdetail>
 // NEW: <div><b>naga-pum</b> meaning(s) sarpa, gaja, sirsa</div>
 //$eid = $matches[1]; // not currently used
 $meanings = $matches[2];  // a,b,c
 $meanings1 = str_replace(',', ', ',$meanings);
 $ans = "<div> synonyms $meanings1</div>";
 return $ans;
}

}

?>
