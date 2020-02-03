#!/usr/bin/perl

use strict;
use warnings;

use CGI;
my $r = new CGI;

print $r->header();
print "pulling repo...<br/>";
system 'git reset --hard origin/HEAD && git pull https://robot-locomotion-bot:build4drake@github.com/RobotLocomotion/6-881-website.git';
print "<br/>done.";
print $r->end_html;
