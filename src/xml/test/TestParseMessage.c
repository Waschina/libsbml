/**
 * \file    TestParseMessage.c
 * \brief   ParseMessage unit tests
 * \author  Ben Bornstein
 *
 * $Id$
 * $Source$
 */
/* Copyright 2002 California Institute of Technology and
 * Japan Science and Technology Corporation.
 *
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published
 * by the Free Software Foundation; either version 2.1 of the License, or
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY, WITHOUT EVEN THE IMPLIED WARRANTY OF
 * MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.  The software and
 * documentation provided hereunder is on an "as is" basis, and the
 * California Institute of Technology and Japan Science and Technology
 * Corporation have no obligations to provide maintenance, support,
 * updates, enhancements or modifications.  In no event shall the
 * California Institute of Technology or the Japan Science and Technology
 * Corporation be liable to any party for direct, indirect, special,
 * incidental or consequential damages, including lost profits, arising
 * out of the use of this software and its documentation, even if the
 * California Institute of Technology and/or Japan Science and Technology
 * Corporation have been advised of the possibility of such damage.  See
 * the GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation,
 * Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.
 *
 * The original code contained here was initially developed by:
 *
 *     Ben Bornstein
 *     The Systems Biology Markup Language Development Group
 *     ERATO Kitano Symbiotic Systems Project
 *     Control and Dynamical Systems, MC 107-81
 *     California Institute of Technology
 *     Pasadena, CA, 91125, USA
 *
 *     http://www.cds.caltech.edu/erato
 *     mailto:sbml-team@caltech.edu
 *
 * Contributor(s):
 */


#include <check.h>

#include "common/common.h"
#include "ParseMessage.h"


START_TEST (test_ParseMessage_create)
{
  ParseMessage_t *pm = ParseMessage_create();


  fail_unless( ParseMessage_getId     (pm) == 0    );
  fail_unless( ParseMessage_getMessage(pm) == NULL );
  fail_unless( ParseMessage_getLine   (pm) == 0    );
  fail_unless( ParseMessage_getColumn (pm) == 0    );

  ParseMessage_free(pm);
}
END_TEST


START_TEST (test_ParseMessage_createWith)
{
  ParseMessage_t *pm = ParseMessage_createWith(1, "Error!", 10, 5);


  fail_unless( !strcmp(ParseMessage_getMessage(pm), "Error!") );

  fail_unless( ParseMessage_getId    (pm) ==  1 );
  fail_unless( ParseMessage_getLine  (pm) == 10 );
  fail_unless( ParseMessage_getColumn(pm) ==  5 );

  ParseMessage_free(pm);
}
END_TEST


START_TEST (test_ParseMessage_free_NULL)
{
  ParseMessage_free(NULL);
}
END_TEST


Suite *
create_suite_ParseMessage (void) 
{ 
  Suite *suite = suite_create("ParseMessage");
  TCase *tcase = tcase_create("ParseMessage");
 

  tcase_add_test(tcase, test_ParseMessage_create     );
  tcase_add_test(tcase, test_ParseMessage_createWith );
  tcase_add_test(tcase, test_ParseMessage_free_NULL  );

  suite_add_tcase(suite, tcase);

  return suite;
}
