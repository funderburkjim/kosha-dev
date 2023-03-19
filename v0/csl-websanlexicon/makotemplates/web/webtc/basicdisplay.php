<?php
error_reporting(E_ALL & ~E_NOTICE & ~E_WARNING);
?>
<?php
/*
// web/webtc/basicdisplay.php
// The main function basicDisplay constructs an HTML table from
// an array of data elements.
// Each of the  data elements is a string which is valid XML.
// The XML is processed using the XML Parser routines (see PHP documentation)
// This XML string is further assumed to be in UTF-8 encoding.
// July 2, 2018 - begin universal version of BasicDisplay.  Objective is
// for this to work for all Cologne dictionaries.
// Aug 7, 2020.  Restructure under assumption that input to
// constructor is either a string or an array of strings.
// Mar 16, 2023. Simplified for kosha-dev
*/
require_once("dbgprint.php");
require_once("parm.php");
class BasicDisplay {
 public $parentEl;
 public $row;
 public $row1;
 public $row1x;
 public $pagecol;
 public $dbg;
 public $inSanskrit;
 public $inkey2;
 public $table;
 public $dict;
 public $sdata; // class to use for Sanskrit
 public $filterin; // transcoding for output
 public $key; // the original key being searched for
 public $basicOption,$serve;
 public $getParms,$status,$html;
public function __construct($key,$string_or_array,$filterin,$dict) {
 
 $this->key = $key;
 $this->dict = $dict;
 $this->filterin = $filterin;
 $this->getParms = new Parm();
 $this->basicOption = $this->getParms->basicOption;
 if ($this->basicOption) {
  $this->serve = "../webtc/servepdf.php";
 } else {
  $this->serve = "servepdf.php";
 }
 
 $this->pagecol="";
 $this->dbg=false;
 $this->inSanskrit=false;
 if ($filterin == "deva") {
 /* use $filterin to generate the class to use for Sanskrit (<s>) text 
    This let's us use siddhanta1 font for Devanagari.
    $this->sdata is used later.
 */
  $this->sdata = "sdata_siddhanta"; // consistent with font.css
 } else {
  $this->sdata = "sdata"; // default.
 }
 // The constructed html is in public variable $table.
 // $this->table is the instance variable
 $this->table = "<h1 class='$sdata'>&nbsp;<SA>$key</SA></h1>\n";

 $this->table .= "<table class='display'>\n";
 if (is_string($string_or_array)) {
  $matches = array($string_or_array);
 }else if (is_array($string_or_array)) {
  if (count($string_or_array) == 0) {
   $matches = array();
  }else {
   // take only first item
   $matches = array($string_or_array[0]);
  }
 }else {
  $matches = array();
 }
 
 $ntot = count($matches);  // either 0 or 1.
 // Associative array. keys are:
 // 
 $this->status = true;
 $this->row = "";
 $this->row1 = "";
 $this->html = "";
 $i = 0;
 while($i<$ntot) {
  $linein=$matches[$i];
  // a line of data from xxx.xml, after adjustments by basicadjust.php
  $line=$linein;  
  
  dbgprint($this->dbg,"basicdisplay: line[$i+1]=$line\n");
  $line=trim($line);
  $l0=strlen($line);
  $this->row = "";
  $this->row1 = "";
  $this->row1x = "";
  $row1x = "";
 
  $this->inSanskrit=false;
  $this->inkey2 = false;
  // initialize parser
  $p = xml_parser_create('UTF-8');
  xml_set_element_handler($p,array($this,'sthndl'),array($this,'endhndl'));
  xml_set_character_data_handler($p,array($this,'chrhndl'));
  xml_parser_set_option($p,XML_OPTION_CASE_FOLDING,FALSE);
  
  dbgprint($this->dbg,"chk 1\n");
  // parse
  if (!xml_parse($p,$line)) {
   dbgprint(true,"basicdisplay.php: xml parse error\nline=$line\n");
   $row = $line;
   $this->status = false;
   $this->html = "<p>basicdisplay.php: xml parse error</p>";
   return;
  }
  dbgprint($this->dbg,"chk 2\n");
  xml_parser_free($p);
  dbgprint($this->dbg,"chk 3\n");
  $this->table .= "<tr>";
  $this->table .= "<td>";
  $style = "";  
  $row1a = "<span style='$style'>{$this->row1}</span>";
  $this->table .= "$row1a\n<br/>{$this->row}\n";
  $this->table .= "</td>";
  // This is so that there will be no need for a horizontal scroll. 12-14-2017
  $this->table .= "<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>";
  $this->table .= "</tr>";
  $i++;
 }
 $this->table .= "</table>\n";
}

 public function getline_key1($line) {
  if (preg_match('|<key1>(.*?)</key1>|',$line,$matches)) {
   $key1 = $matches[1];
   return $key1;
  }else {
   return $this->key;
  }
 }

 public function sthndl_div($attribs) {
  // 07-05-2018. Handle various kinds of div elements
  // based on 'n' attribute and diction.
  if (isset($attribs['style'])) {
   $style=$attribs['style'];
   $ans = "<div style='$style'>";
  } else {
   $ans = "<div>";
  }
  return $ans;

 }
 public function sthndl($xp,$el,$attribs) {
  // $el is one of the elements of the xml record.
  // 
  if (preg_match('/^H.+$/',$el)) {
   // don't display
  } else if ($el == "s")  {
   $this->inSanskrit = true;
  } else if ($el == "key2"){
   $this->inkey2 = true;
  } else if ($el == "b"){ 
   $this->row .= "<strong>"; 
  } else if ($el == "lex"){ // m. f., etc.
   $this->row .= "<strong>"; 
  } else if ($el == "i"){
   $this->row .= "<i>"; 
  } else if ($el == "br"){
   $this->row .= "<br/>";   
  } else if ($el == "h"){
  } else if ($el == "body"){
  } else if ($el == "tail"){
  } else if ($el == "L"){
  } else if ($el == "info") { 
  } else if ($el == "pc"){
  } else if ($el == "pb"){
  } else if ($el == "key1"){
  } else if ($el == "hom"){ // handled wholly in chrhndl
  } else if ($el == "symbol") {
  } else if ($el == "div") {
   $this->row .= $this->sthndl_div($attribs);
  } else if ($el == "lb") {
    $this->row .= "<br/>";
  } else if ($el == "span") {
   if (isset($attribs['class'])) {
    $class = $attribs['class'];
    $this->row .= "<span class='$class'>";
   } else if (isset($attribs['style'])) {
    $style = $attribs['style'];
    $this->row .= "<span style='$style'>";
   } else {
   $this->row .= "<span>";
   }
  } else if ($el == "sic") {
   // no rendering
  } else if ($el == "ab"){
    if (isset($attribs['n'])) {
     // local abbreviation <ab n="tooltip for X.">X.</ab>
     $tran = $attribs['n'];
     $style = "border-bottom: 1px dotted #000; text-decoration: none;";
     $this->row .= "<span title='$tran' style='$style'>";
    }else {
     // <ab>X.</ab>  tooltip from dictionary abbreviations database
     $this->row .= "<span>";
    }
  } else {
    // $el unrecognized
    $this->row .= "<br/>&lt;$el&gt;";
  }

  $this->parentEl = $el;  // used by chrhndl
}

 public function endhndl($xp,$el) {
  $this->parentEl = "";
  if ($el == "s") {
   $this->inSanskrit = false;
  } else if ($el == "F") {
   $this->row .= "]</span>&nbsp;<br/>";
  } else if ($el == "b"){ 
   $this->row .= "</strong>"; 
  } else if ($el == "graverse") {
   $this->row .= "</span>";
  } else if ($el == "gralink") {
   $this->row .= "</a>";
  } else if ($el == "lanlink") {
   $this->row .= "</a>";
  } else if ($el == "lex"){
   $this->row .= "</strong>"; 
  } else if ($el == "i"){
   $this->row .= "</i>"; 
  } else if ($el == "pb"){
  } else if ($el == "key2") {
   $this->inkey2 = false;
  } else if ($el == "symbol") {
  } else if ($el == "div") {
   // close the div
    $this->row .= "</div>"; 
 } else if ($el == "ls") {
   $this->row .= "</span>&nbsp;";
  } else if ($el == "span") {
   $this->row .= "</span>";
  } else if ($el == "ab") {
   $this->row .= "</span>";
  } 
 }

 public function chrhndl($xp,$data) {
  $sdata = $this->sdata;
  if ($this->parentEl == "key1"){ // nothing printed
  } else if ($this->parentEl == "key2"){
  } else if ($this->parentEl == "pb") {
   $hrefdata = $this->getHrefPage($data);
   $style = "font-size:smaller; font-weight:bold;";
   $this->row .= "<span style='$style'> $hrefdata</span>";   
  } else if ($this->parentEl == "pc") {
   $hrefdata = $this->getHrefPage($data);
   $style = "font-size:normal; color:rgb(160,160,160);";
   $this->row1 .= "<span style='$style'> [Printed book page $hrefdata]</span>";
  } else if ($this->parentEl == "L") {
   $style = "font-size:normal; color:rgb(160,160,160);";
   $this->row1 .= "<span style='$style'> [Cologne record ID=$data]</span>";
  } else if ($this->parentEl == 's') {
   $this->row .= "<span class='$sdata'><SA>$data</SA></span>";
  } else if ($this->inSanskrit) {
   // probably not needed
   $this->row .= "<span class='$sdata'><SA>$data</SA></span>";
  } else if ($this->parentEl == "ab") {
   $this->row .= "$data";
  }else if ($this->parentEl == "ls") { 
   $this->row .= $data;
  } else { // Arbitrary other text
   $this->row .= $data;
   dbgprint($this->dbg,"chrhdl: data = $data, parentEl = {$this->parentEl}\n");
  }
}
public function getHrefPage($data) {
/* getHrefPage generates markup for the link to a program which displays a pdf, as
 specified by the  input argument '$data'.
 In this implementation, the program which serves the pdf is
 $serve = ../webtc/servepdf.php.
 $data is assumed to be a string with a comma-delimited list of page numbers,
 only the first of which is used to generate a link.
 The markup returned for a given $lnum in the list $data is
   <a href='$serve?page=$lnum' target='_Blank'>$lnum</a>
 It is up to $serve to associate $lnum with a file.

*/
  $ans="";
 //$lnums = preg_split('/[,-]/',$data);
 $serve = $this->serve;
 $lnums = preg_split('/[,]/',$data);  //%{pfx}
 foreach($lnums as $lnum) {
  #list($page,$col) =  preg_split('/[-]/',$lnum);
  $page = $lnum; # this may be dictionary specific.
  if ($ans == "") {
   $dict = $this->dict;
   $args = "dict=$dict&page=$page";
   #$ans = "<a href='$serve?$args' target='_Blank'>$lnum</a>";
   $dictup = strtoupper($dict);
   $style = "color:rgb(130,130,130);";
   $ans = "<a href='$serve?$args' target='_$dictup' style='$style'>$lnum</a>";
  }else {
   $ans .= ",$lnum";
  }
 }
 return $ans;
}


} ## end of class 
?>
