# Description : sbmlmanual.perl
# Author(s)   : Michael Hucka <mhucka@@cds.caltech.edu>
# Organization: CDS, California Institute of Technology
# Created     : 2000-09-27 16:57 PDT
# Revision    : $Id$
# $Source$
#
# Based on cekarticle.perl which I wrote and which was in turn originally
# based on article.perl by Ross Moore <ross@mpce.mq.edu.au> 09-14-97

package main;

&do_require_package('article');
&do_require_package('array');
&do_require_package('alltt');
&do_require_package('booktabs');
&do_require_package('verbatim');
&do_require_package('color');
&do_require_package('graphicx');
&do_require_package('html');
&do_require_package('hyperref');
&do_require_package('natbib');
&do_require_package('listings');

#-----------------------------------------------------------------------------
# Stuff from basic article.perl/article.cls.
#-----------------------------------------------------------------------------

sub do_sbmlmanual_a4paper{}
sub do_sbmlmanual_a5paper{}
sub do_sbmlmanual_b5paper{}
sub do_sbmlmanual_legalpaper{}
sub do_sbmlmanual_letterpaper{}
sub do_sbmlmanual_executivepaper{}
sub do_sbmlmanual_landscape{}
sub do_sbmlmanual_final{}
sub do_sbmlmanual_draft{}
sub do_sbmlmanual_oneside{}
sub do_sbmlmanual_twoside{}
sub do_sbmlmanual_openright{}
sub do_sbmlmanual_openany{}
sub do_sbmlmanual_onecolumn{}
sub do_sbmlmanual_twocolumn{}
sub do_sbmlmanual_notitlepage{}
sub do_sbmlmanual_titlepage{}
sub do_sbmlmanual_openbib{}

sub do_sbmlmanual_10pt{ $LATEX_FONT_SIZE = '10pt' unless $LATEX_FONT_SIZE; }
sub do_sbmlmanual_11pt{ $LATEX_FONT_SIZE = '11pt' unless $LATEX_FONT_SIZE; }
sub do_sbmlmanual_12pt{ $LATEX_FONT_SIZE = '12pt' unless $LATEX_FONT_SIZE; }

sub do_sbmlmanual_leqno{ $EQN_TAGS = 'L'; }
sub do_sbmlmanual_reqno{ $EQN_TAGS = 'R'; }
sub do_sbmlmanual_fleqn{ $FLUSH_EQN = 1; }

sub do_cmd_thesection {
    join('', &do_cmd_arabic("${O}0${C}section${O}0$C"), @_[0]) }
sub do_cmd_thesubsection {
    join('',&translate_commands("\\thesection")
	,".", &do_cmd_arabic("${O}0${C}subsection${O}0$C"), @_[0]) }
sub do_cmd_thesubsubsection {
    join('',&translate_commands("\\thesubsection")
	,"." , &do_cmd_arabic("${O}0${C}subsubsection${O}0$C"), @_[0]) }
sub do_cmd_theparagraph {
    join('',&translate_commands("\\thesubsubsection")
	,"." , &do_cmd_arabic("${O}0${C}paragraph${O}0$C"), @_[0]) }
sub do_cmd_thesubparagraph {
    join('',&translate_commands("\\theparagraph")
	,"." , &do_cmd_arabic("${O}0${C}subparagraph${O}0$C"), @_[0]) }

sub do_cmd_theequation {
    join('', &do_cmd_arabic("${O}0${C}equation${O}0$C"), @_[0]) }

sub do_cmd_thefootnote {
    join('', &do_cmd_arabic("${O}0${C}footnote${O}0$C"), @_[0]) }

sub do_cmd_thefigure {
    join('', &do_cmd_arabic("${O}0${C}figure${O}0$C"), @_[0]) }

sub do_cmd_thetable {
    join('',  &do_cmd_arabic("${O}0${C}table${O}0$C"), @_[0]) }

#-----------------------------------------------------------------------------
# Additions for sbmlmanual.cls
#-----------------------------------------------------------------------------

$notoc = 0;

# Run this directly in order to get a white background in latex2html.
&apply_body_options("BGCOLOR", "ffffff");

sub do_sbmlmanual_toc{}
sub do_sbmlmanual_notoc{ $notoc++; }

sub do_cmd_attrib { &styled_text_chunk('TT','','font','','', '', @_); }
sub do_cmd_attribtype { &styled_text_chunk('TT','','font','','', '', @_); }
sub do_cmd_attribvalue { &styled_text_chunk('TT','','font','','', '', @_); }
sub do_cmd_class { &styled_text_chunk('TT','','font','','', '', @_); }
sub do_cmd_method { &styled_text_chunk('TT','','font','','', '', @_); }
sub do_cmd_variable { &styled_text_chunk('TT','','font','','', '', @_); }
sub do_cmd_shell { &styled_text_chunk('TT','','font','','', '', @_); }
sub do_cmd_code { &styled_text_chunk('TT','','font','','', '', @_); }

# There must be more direct ways of making \toprule etc be essentially
# ignored, but this is the best I could do without spending more time on it.

sub do_cmd_toprule {
    local($_) = @_;
    &ignore_numeric_argument;
    local($pre,$post) = &minimize_open_tags('');
    join('',$pre,$_);
}

sub do_cmd_midrule {
    local($_) = @_;
    &ignore_numeric_argument;
    local($pre,$post) = &minimize_open_tags('');
    join('',$pre,$_);
}
sub do_cmd_bottomrule {
    local($_) = @_;
    &ignore_numeric_argument;
    local($pre,$post) = &minimize_open_tags('');
    join('',$pre,$_);
}

sub do_cmd_tightspacing {
    local($_) = @_;
    &ignore_numeric_argument;
    local($pre,$post) = &minimize_open_tags('<BR>');
    join('',$pre,$_);
}

sub do_cmd_regularspacing {
    local($_) = @_;
    &ignore_numeric_argument;
    local($pre,$post) = &minimize_open_tags('');
    join('',$pre,$_);
}

# Titlepage stuff.
# latex2html base code already defines do_cmd_{title,author,address}.

# A version of the each of the following is defined by the latex2html base
# code, but it produces a mailto: link.  We don't want that because we put
# multiple email addresses in \email{}.

sub do_cmd_authoremail {
    local($_) = @_;
    &get_next_optional_argument;
    local($next);
    $next = &missing_braces unless (
	(s/$next_pair_pr_rx/$next = $2;''/eo)
	||(s/$next_pair_rx/$next = $2;''/eo));
    ($t_email) = &translate_commands($next);
    $_;
}

sub do_cmd_acknowledge {
    local($_) = @_;
    &get_next_optional_argument;
    local($next);
    $next = &missing_braces unless (
	(s/$next_pair_pr_rx/$next = $2;''/eo)
	||(s/$next_pair_rx/$next = $2;''/eo));
    ($t_acknowledge) = &simplify(&translate_commands($next));
    $_;
}

# This redefines the do_cmd_maketitlepage() from the latex2html base code in
# order to handle our specialized constructs and layout.

sub do_cmd_maketitlepage {
    local($_) = @_;
    local($the_title) = '';
    local($alignc, $alignl);
    if ($HTML_VERSION > 2.1) {
	$alignc = " ALIGN=\"CENTER\""; 
	$alignl = " ALIGN=\"LEFT\""; 
    }
    if ($t_title) {
	$the_title .= "<HR NOSHADE SIZE=1 WIDTH=\"80%\">";
	$the_title .= "<H1$alignc>";
	$the_title .= $t_title;
	$the_title .= "</H1>\n";
	$the_title .= "<HR NOSHADE SIZE=1 WIDTH=\"80%\">";
    } else { &write_warnings("\nThis document has no title."); }
    if ($t_author) {
	if ($t_authorURL) {
	    local($href) = &translate_commands($t_authorURL);
	    $href = &make_named_href('author'
		         , $href, "<STRONG>${t_author}</STRONG>");
	    $the_title .= "\n<P$alignc>$href</P>";
	} else {
	    $the_title .= "\n<P$alignc><STRONG>$t_author</STRONG></P>";
	}
    } else { &write_warnings("\nThere is no author for this document."); }
    if ($t_email&&!($t_email=~/^\s*(($O|$OP)\d+($C|$CP))\s*\1\s*$/)) {
        $the_title .= "\n<P$alignc><TT>$t_email</TT></P>";}
    if ($t_affil&&!($t_affil=~/^\s*(($O|$OP)\d+($C|$CP))\s*\1\s*$/)) {
	$the_title .= "\n<P$alignc><I>$t_affil</I></P>";}
    if ($t_address&&!($t_address=~/^\s*(($O|$OP)\d+($C|$CP))\s*\1\s*$/)) {
        $the_title .= "\n<P$alignc>$t_address</P>";}
    if ($t_acknowledge&&!($t_acknowledge=~/^\s*(($O|$OP)\d+($C|$CP))\s*\1\s*$/)) {
        $the_title .= "\n<P$alignc><SMALL>$t_acknowledge</SMALL></P>";}
    if ($t_date&&!($t_date=~/^\s*(($O|$OP)\d+($C|$CP))\s*\1\s*$/)) {
	$the_title .= "\n<P$alignc><STRONG>$t_date</STRONG></P>";}

    # Add the funding acknowledgments and logo graphics.

    $the_title .= "<BR><BR>";
    open(ACK, "../../../FUNDING.txt") || die "Can't open FUNDING.txt file.";
    undef $/;
    $the_title .= "<BLOCKQUOTE><SMALL>" . <ACK> . "</SMALL></BLOCKQUOTE>";
    close(ACK);

    $the_title .= "<BR><BR>";
    $the_title .= "<CENTER><IMG SRC=\"sbml-logo-300x48.jpg\"></CENTER>";

    # Add the table of contents.
    # FIXME: this should test for $notoc
    $_ .= $the_title;
    $_ .= &do_cmd_tableofcontents();
}

# This redefines the do_cmd_maketitle() from the latex2html base code in
# order to handle our specialized constructs and layout.  This is basically
# identical to do_cmd_maketitlepage, but doesn't insert a table of contents.

sub do_cmd_maketitle {
    local($_) = @_;
    local($the_title) = '';
    local($alignc, $alignl);
    if ($HTML_VERSION > 2.1) {
	$alignc = " ALIGN=\"CENTER\""; 
	$alignl = " ALIGN=\"LEFT\""; 
    }
    if ($t_title) {
	$the_title .= "<HR NOSHADE>\n<H1$alignc>$t_title</H1>\n<HR NOSHADE>";
    } else { &write_warnings("\nThis document has no title."); }
    if ($t_author) {
	if ($t_authorURL) {
	    local($href) = &translate_commands($t_authorURL);
	    $href = &make_named_href('author'
		         , $href, "<STRONG>${t_author}</STRONG>");
	    $the_title .= "\n<P$alignc>$href</P>";
	} else {
	    $the_title .= "\n<P$alignc><STRONG>$t_author</STRONG></P>";
	}
    } else { &write_warnings("\nThere is no author for this document."); }
    if ($t_email&&!($t_email=~/^\s*(($O|$OP)\d+($C|$CP))\s*\1\s*$/)) {
        $the_title .= "\n<P$alignc><TT>$t_email</TT></P>";}
    if ($t_affil&&!($t_affil=~/^\s*(($O|$OP)\d+($C|$CP))\s*\1\s*$/)) {
	$the_title .= "\n<P$alignc><I>$t_affil</I></P>";}
    if ($t_address&&!($t_address=~/^\s*(($O|$OP)\d+($C|$CP))\s*\1\s*$/)) {
        $the_title .= "\n<P$alignc>$t_address</P>";}
    if ($t_acknowledge&&!($t_acknowledge=~/^\s*(($O|$OP)\d+($C|$CP))\s*\1\s*$/)) {
        $the_title .= "\n<P$alignc><SMALL>$t_acknowledge</SMALL></P>";}
    if ($t_date&&!($t_date=~/^\s*(($O|$OP)\d+($C|$CP))\s*\1\s*$/)) {
	$the_title .= "\n<P$alignc><STRONG>$t_date</STRONG></P>";}
    # Add the table of contents.
    # FIXME: this should test for $notoc
    $_ .= $the_title;
}

# Copied from do_cmd_ref from latex2html $Id: latex2html.pin,v 1.62.

sub do_cmd_vref {
    local($_) = @_;
    &process_ref($cross_ref_mark,$cross_ref_mark);
}

# Misc. commands.

sub do_cmd_texttrademark { join('', '&#153;', $_[0]); }

# FIXME: the next one doesn't actually work.

sub do_cmd_textsuperscript {
  local($_) = @_;
  local($next);
  $next = &missing_braces
    unless ( (s/$next_pair_pr_rx/$next = $2;''/eo)
	     || (s/$next_pair_rx/$next = $2;''/eo)
	   );
  ($next) = &translate_commands($next);
  "<SUP>$text</SUP>" . $_;
}

# Some additional commands for hyperref commands that apparently aren't
# provided in latex2html's hyperref bindings.

# 2003-07-27 <mhucka@caltech.edu> Pulled from html.perl v1.38

sub do_cmd_href{
    local($_) = @_;
    local($text, $url, $href);
    local($name, $dummy) = &get_next_optional_argument;
    $text = &missing_braces unless
	((s/$next_pair_pr_rx/$url = $2; ''/eo)
	||(s/$next_pair_rx/$url = $2; ''/eo));
    $url = &missing_braces unless
	((s/$next_pair_pr_rx/$text = $2; ''/eo)
	||(s/$next_pair_rx/$text = $2; ''/eo));
    $*=1; s/^\s+/\n/; $*=0;
    if ($name) { $href = &make_named_href($name,$url,$text) }
    else { $href = &make_href($url,$text) }
    print "\nHREF:$href" if ($VERBOSITY > 3);
    join ('',$href,$_);
}

# 2004-09-17 <mhucka@caltech.edu>
# Pulled from latex2html.  I didn't like the way the original used <small>
# around small caps fonts.

sub process_smallcaps {
    local($text) = @_;
    local($next, $scstr, $scbef, $special, $char);
    # is this enough for \sc and \scshape ?
    $text = &translate_environments($text);

    # MRO: replaced $* with /m
    while ($text =~ /(\\[a-zA-Z]+|[&;]SPM\w+;|<[^>]+>)+/m ) {
	$scbef = $`; $special = $&; $text = $';
	while ( $scbef =~ /(&#\d+;|[a-z$sclower])+[a-z\W\d$sclower]*/m) {
	    $scstr .= $`; $scbef = $';
	    $next = $&; 
	    $next =~ s/&#(\d+);/&lowercase_entity($1)/egm;
	    eval "\$next =~ $scextra" if ($scextra);
	    eval "\$next =~ tr/a-z$sclower/A-Z$scupper/";
	    $scstr .= $next;
	}
	$scstr .= $scbef . $special;
    }
    if ($text) {
	while ( $text =~ /(&#\d+;|[a-z$sclower])+[a-z\W\d$sclower]*/m) {
	    $scstr .= $`; $text = $';
	    $next = $&;
	    $next =~ s/&#(\d+);/&lowercase_entity($1)/egm;
	    eval "\$next =~ $scextra" if ($scextra);
	    eval "\$next =~ tr/a-z$sclower/A-Z$scupper/";
	    $scstr .= $next;
	}
	$scstr .= $text;
    }
    $scstr;
}

# 2004-09-20 <mhucka@caltech.edu>
# Pulled from alltt.perl and modified to create the 'example' environment.

sub preprocess_alltt {
    local ($before, $after, $example, $example_env);
    local ($example_begin) = "<example_begin>";
    local ($example_end) = "<example_end>";
    local($saveRS) = $/; $*=1;undef $/;
    while (/\\begin\s*{($example_rx)}([ \t]*\n)?/m) {
	$example_env = $1;
	$example = "";
	($before, $after) = ($`, $');
	if ($after =~ /\\end\s*{($example_rx)}/s) {
	    ($example, $after) = ($`, $');
	    local(@check) = split("\n",$before);
	    local($lastline) = pop @check unless ($before =~ s/\n$//s);
	    $example = &example_helper($example)	 # shield special chars
		unless ($lastline =~ /(^|[^\\])(\\\\)*%.*$/m);  # unless commented out
	    undef @check; undef $lastline;
	}
	$_ = join('', $before, "\n", $example_begin, "{$example_env}\n"
		, $example, $example_end, "{$example_env}", $after);
    }
    $/ = $saveRS;
    s/$example_begin\{([^\}]*)\}/\\begin{$1}/gos;
    s/$example_end\{([^\}]*)\}/\\end{$1}/gos;
}

sub example_helper {
    local ($_) = @_;
    local($br_id) = ++$global{'max_id'};
    s/^/\\relax$O$br_id$C$O$br_id$C /s; # Preserve leading & trailing white space
    s/\t/ /g;		# Remove tabs
    # preserve space after macro names
    s/(\\\w+) /$br_id=++$global{'max_id'};$1."$O$br_id$C$O$br_id$C "/eg;
    s/\\?\$/;SPMdollar;/g;
    s/\\?%/;SPMpct;/g;
    # protect " from being used as an active character with some languages
    s/((^|[^\\])(\\\\)*)(\"|\;SPMquot\;)/$1\&#34;/gm;
    s/~/;SPMtilde;/g;
    s/\n/\n<BR>/g;	# preserve end-of-lines --- cannot have <P>s
    join('', $_, "\\relax ");
}

sub do_env_example {
    local ($_) = @_;
    local($closures,$reopens,$example_start,$example_end,@open_block_tags);
    &get_next_optional_argument;
    if ($HTML_VERSION > 3.0) {
        if ($USING_STYLES) {
            $env_id .= ' CLASS="example"' unless ($env_id =~/CLASS=/);
            $env_style{'example'} = " " unless ($env_style{'example'});
        }
	$example_start = "\n<DIV$env_id ALIGN=\"LEFT\">\n";
	$example_end = "\n</DIV>\n";
	$env_id = '';
    } else {
	$example_start = "<P ALIGN=\"LEFT\">";
	$example_end = "</P>";
    }


    # get the tag-strings for all open tags
    local(@keep_open_tags) = @$open_tags_R;
    ($closures,$reopens) = &preserve_open_tags() if (@$open_tags_R);

    # get the tags for text-level tags only
    $open_tags_R = [ @keep_open_tags ];
    local($local_closures, $local_reopens);
    ($local_closures, $local_reopens,@open_block_tags) = &preserve_open_block_tags
	if (@$open_tags_R);

    $open_tags_R = [ @open_block_tags ];

    do {
	local($open_tags_R) = [ @open_block_tags ];
	local(@save_open_tags) = ();

	local($cnt) = ++$global{'max_id'};
	$_ = join('',"$O$cnt$C\\tt$O", ++$global{'max_id'}, $C
		, "<PRE>" . $_ . "</PRE>" 
		  , $O, $global{'max_id'}, "$C$O$cnt$C");

	$_ = &translate_environments($_);
	$_ = &translate_commands($_) if (/\\/);

	# preserve space-runs, using &nbsp;
	while (s/(\S) ( +)/$1$2;SPMnbsp;/g){};
	s/(<BR>) /$1;SPMnbsp;/g;

	$_ = join('', $closures, $example_start , $local_reopens
		, $_
		, &balance_tags() #, $local_closures
		, $example_end, $reopens);
	undef $open_tags_R; undef @save_open_tags;
    };

    $open_tags_R = [ @keep_open_tags ];
    $_;
}

#-----------------------------------------------------------------------------
# End of file.
#-----------------------------------------------------------------------------

1;	# Must be last line
