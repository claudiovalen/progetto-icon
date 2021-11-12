# bc_simple_rules_questions_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def what_malattia_Oidio(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_Oidio: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              with engine.prove('questions', 'clima_umido', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_Oidio: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'vedi_colore_grappoli', context,
                                    (rule.pattern(1),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_Oidio: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'colore_grappoli', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_Oidio: got unexpected plan from when clause 5"
                          if context.lookup_data('ans2') in (2,):
                            with engine.prove('questions', 'acini_spaccati', context,
                                              (rule.pattern(1),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "bc_simple_rules_questions.what_malattia_Oidio: got unexpected plan from when clause 7"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_Flavescenza_Dorata(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_Flavescenza_Dorata: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              with engine.prove('questions', 'clima_umido', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_Flavescenza_Dorata: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'vedi_colore_grappoli', context,
                                    (rule.pattern(2),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_Flavescenza_Dorata: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'colore_grappoli', context,
                                        (rule.pattern(3),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_Flavescenza_Dorata: got unexpected plan from when clause 5"
                          if context.lookup_data('ans2') in (1,):
                            with engine.prove('questions', 'tralci_gommosi', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "bc_simple_rules_questions.what_malattia_Flavescenza_Dorata: got unexpected plan from when clause 7"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_Botrite(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_Botrite: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              with engine.prove('questions', 'clima_umido', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_Botrite: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'vedi_colore_grappoli', context,
                                    (rule.pattern(1),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_Botrite: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'colore_grappoli', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_Botrite: got unexpected plan from when clause 5"
                          if context.lookup_data('ans2') in (2,):
                            with engine.prove('questions', 'acini_spaccati', context,
                                              (rule.pattern(3),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "bc_simple_rules_questions.what_malattia_Botrite: got unexpected plan from when clause 7"
                                with engine.prove('questions', 'grappoli_caduti', context,
                                                  (rule.pattern(1),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "bc_simple_rules_questions.what_malattia_Botrite: got unexpected plan from when clause 8"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_Peronospora(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_Peronospora: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              with engine.prove('questions', 'clima_umido', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_Peronospora: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'vedi_colore_grappoli', context,
                                    (rule.pattern(1),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_Peronospora: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'vedi_colore_foglie', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_Peronospora: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'colore_foglie', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "bc_simple_rules_questions.what_malattia_Peronospora: got unexpected plan from when clause 6"
                              if context.lookup_data('ans2') in (1,):
                                with engine.prove('questions', 'muffa_bianca', context,
                                                  (rule.pattern(2),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "bc_simple_rules_questions.what_malattia_Peronospora: got unexpected plan from when clause 8"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_Mal_dell_esca(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_Mal_dell_esca: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              with engine.prove('questions', 'clima_umido', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_Mal_dell_esca: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'vedi_colore_grappoli', context,
                                    (rule.pattern(1),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_Mal_dell_esca: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'vedi_colore_foglie', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_Mal_dell_esca: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'colore_foglie', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "bc_simple_rules_questions.what_malattia_Mal_dell_esca: got unexpected plan from when clause 6"
                              if context.lookup_data('ans2') in (2,):
                                with engine.prove('questions', 'spaccature_longitudinali', context,
                                                  (rule.pattern(2),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "bc_simple_rules_questions.what_malattia_Mal_dell_esca: got unexpected plan from when clause 8"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_Marciume_acido(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_Marciume_acido: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              with engine.prove('questions', 'clima_umido', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_Marciume_acido: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'vedi_colore_grappoli', context,
                                    (rule.pattern(1),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_Marciume_acido: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'colore_grappoli', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_Marciume_acido: got unexpected plan from when clause 5"
                          if context.lookup_data('ans2') in (2,):
                            with engine.prove('questions', 'acini_spaccati', context,
                                              (rule.pattern(3),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "bc_simple_rules_questions.what_malattia_Marciume_acido: got unexpected plan from when clause 7"
                                with engine.prove('questions', 'grappoli_caduti', context,
                                                  (rule.pattern(3),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "bc_simple_rules_questions.what_malattia_Marciume_acido: got unexpected plan from when clause 8"
                                    with engine.prove('questions', 'odore_aceto', context,
                                                      (rule.pattern(1),)) \
                                      as gen_9:
                                      for x_9 in gen_9:
                                        assert x_9 is None, \
                                          "bc_simple_rules_questions.what_malattia_Marciume_acido: got unexpected plan from when clause 9"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_Arricciamento_vite(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_Arricciamento_vite: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              with engine.prove('questions', 'clima_umido', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_Arricciamento_vite: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'vedi_colore_grappoli', context,
                                    (rule.pattern(1),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_Arricciamento_vite: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'vedi_colore_foglie', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_Arricciamento_vite: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'crescita_zigzagante', context,
                                            (rule.pattern(2),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "bc_simple_rules_questions.what_malattia_Arricciamento_vite: got unexpected plan from when clause 6"
                              rule.rule_base.num_bc_rule_successes += 1
                              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_fioretta(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_fioretta: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              with engine.prove('questions', 'vino_opaco', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_fioretta: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'velo_chiaro', context,
                                    (rule.pattern(1),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_fioretta: got unexpected plan from when clause 4"
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_spunto(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_spunto: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              with engine.prove('questions', 'vino_opaco', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_spunto: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'gusto_aceto', context,
                                    (rule.pattern(2),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_spunto: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'quanto_aceto', context,
                                        (rule.pattern(3),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_spunto: got unexpected plan from when clause 5"
                          if context.lookup_data('ans2') in (1,):
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_acescenza(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_acescenza: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              with engine.prove('questions', 'vino_opaco', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_acescenza: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'gusto_aceto', context,
                                    (rule.pattern(2),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_acescenza: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'quanto_aceto', context,
                                        (rule.pattern(3),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_acescenza: got unexpected plan from when clause 5"
                          if context.lookup_data('ans2') in (2,):
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_girato(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_girato: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              with engine.prove('questions', 'vino_opaco', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_girato: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'velo_chiaro', context,
                                    (rule.pattern(2),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_girato: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'torbido_smorto', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_girato: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'tipo_vino', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "bc_simple_rules_questions.what_malattia_girato: got unexpected plan from when clause 6"
                              if context.lookup_data('ans2') in (1,):
                                with engine.prove('questions', 'vino_amaro', context,
                                                  (rule.pattern(2),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "bc_simple_rules_questions.what_malattia_girato: got unexpected plan from when clause 8"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_filante(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_filante: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              with engine.prove('questions', 'vino_opaco', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_filante: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'velo_chiaro', context,
                                    (rule.pattern(2),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_filante: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'torbido_smorto', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_filante: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'tipo_vino', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "bc_simple_rules_questions.what_malattia_filante: got unexpected plan from when clause 6"
                              if context.lookup_data('ans2') in (2,):
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_malattia_amarore(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'scelta_malattia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_malattia_amarore: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              with engine.prove('questions', 'vino_opaco', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_simple_rules_questions.what_malattia_amarore: got unexpected plan from when clause 3"
                  with engine.prove('questions', 'velo_chiaro', context,
                                    (rule.pattern(2),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc_simple_rules_questions.what_malattia_amarore: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'torbido_smorto', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc_simple_rules_questions.what_malattia_amarore: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'tipo_vino', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "bc_simple_rules_questions.what_malattia_amarore: got unexpected plan from when clause 6"
                              if context.lookup_data('ans2') in (1,):
                                with engine.prove('questions', 'vino_amaro', context,
                                                  (rule.pattern(1),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "bc_simple_rules_questions.what_malattia_amarore: got unexpected plan from when clause 8"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_simple_rules_questions')
  
  bc_rule.bc_rule('what_malattia_Oidio', This_rule_base, 'quale_malattia',
                  what_malattia_Oidio, None,
                  (pattern.pattern_literal('Oidio'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(True),
                   contexts.variable('ans2'),))
  
  bc_rule.bc_rule('what_malattia_Flavescenza_Dorata', This_rule_base, 'quale_malattia',
                  what_malattia_Flavescenza_Dorata, None,
                  (pattern.pattern_literal('Flavescenza_Dorata'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans2'),))
  
  bc_rule.bc_rule('what_malattia_Botrite', This_rule_base, 'quale_malattia',
                  what_malattia_Botrite, None,
                  (pattern.pattern_literal('Botrite'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(True),
                   contexts.variable('ans2'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_malattia_Peronospora', This_rule_base, 'quale_malattia',
                  what_malattia_Peronospora, None,
                  (pattern.pattern_literal('Peronospora'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans2'),))
  
  bc_rule.bc_rule('what_malattia_Mal_dell_esca', This_rule_base, 'quale_malattia',
                  what_malattia_Mal_dell_esca, None,
                  (pattern.pattern_literal('Mal_dell_esca'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans2'),))
  
  bc_rule.bc_rule('what_malattia_Marciume_acido', This_rule_base, 'quale_malattia',
                  what_malattia_Marciume_acido, None,
                  (pattern.pattern_literal('Marciume_acido'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(True),
                   contexts.variable('ans2'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_malattia_Arricciamento_vite', This_rule_base, 'quale_malattia',
                  what_malattia_Arricciamento_vite, None,
                  (pattern.pattern_literal('Arricciamento_vite'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_malattia_fioretta', This_rule_base, 'quale_malattia',
                  what_malattia_fioretta, None,
                  (pattern.pattern_literal('fioretta'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_malattia_spunto', This_rule_base, 'quale_malattia',
                  what_malattia_spunto, None,
                  (pattern.pattern_literal('spunto'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans2'),))
  
  bc_rule.bc_rule('what_malattia_acescenza', This_rule_base, 'quale_malattia',
                  what_malattia_acescenza, None,
                  (pattern.pattern_literal('acescenza'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans2'),))
  
  bc_rule.bc_rule('what_malattia_girato', This_rule_base, 'quale_malattia',
                  what_malattia_girato, None,
                  (pattern.pattern_literal('girato'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans2'),))
  
  bc_rule.bc_rule('what_malattia_filante', This_rule_base, 'quale_malattia',
                  what_malattia_filante, None,
                  (pattern.pattern_literal('filante'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans2'),))
  
  bc_rule.bc_rule('what_malattia_amarore', This_rule_base, 'quale_malattia',
                  what_malattia_amarore, None,
                  (pattern.pattern_literal('amarore'),),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans2'),))


Krb_filename = '..\\kb\\bc_simple_rules_questions.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((26, 26), (7, 7)),
    ((27, 32), (8, 8)),
    ((33, 38), (9, 9)),
    ((39, 44), (10, 10)),
    ((45, 45), (11, 11)),
    ((46, 51), (12, 12)),
    ((64, 68), (15, 15)),
    ((70, 75), (17, 17)),
    ((76, 76), (18, 18)),
    ((77, 82), (19, 19)),
    ((83, 88), (20, 20)),
    ((89, 94), (21, 21)),
    ((95, 95), (22, 22)),
    ((96, 101), (23, 23)),
    ((114, 118), (26, 26)),
    ((120, 125), (28, 28)),
    ((126, 126), (29, 29)),
    ((127, 132), (30, 30)),
    ((133, 138), (31, 31)),
    ((139, 144), (32, 32)),
    ((145, 145), (33, 33)),
    ((146, 151), (34, 34)),
    ((152, 157), (35, 35)),
    ((170, 174), (38, 38)),
    ((176, 181), (40, 40)),
    ((182, 182), (41, 41)),
    ((183, 188), (42, 42)),
    ((189, 194), (43, 43)),
    ((195, 200), (44, 44)),
    ((201, 206), (45, 45)),
    ((207, 207), (46, 46)),
    ((208, 213), (47, 47)),
    ((226, 230), (50, 50)),
    ((232, 237), (52, 52)),
    ((238, 238), (53, 53)),
    ((239, 244), (54, 54)),
    ((245, 250), (55, 55)),
    ((251, 256), (56, 56)),
    ((257, 262), (57, 57)),
    ((263, 263), (58, 58)),
    ((264, 269), (59, 59)),
    ((282, 286), (62, 62)),
    ((288, 293), (64, 64)),
    ((294, 294), (65, 65)),
    ((295, 300), (66, 66)),
    ((301, 306), (67, 67)),
    ((307, 312), (68, 68)),
    ((313, 313), (69, 69)),
    ((314, 319), (70, 70)),
    ((320, 325), (71, 71)),
    ((326, 331), (72, 72)),
    ((344, 348), (76, 76)),
    ((350, 355), (78, 78)),
    ((356, 356), (79, 79)),
    ((357, 362), (80, 80)),
    ((363, 368), (81, 81)),
    ((369, 374), (82, 82)),
    ((375, 380), (83, 83)),
    ((393, 397), (86, 86)),
    ((399, 404), (88, 88)),
    ((405, 405), (89, 89)),
    ((406, 411), (90, 90)),
    ((412, 417), (91, 91)),
    ((430, 434), (94, 94)),
    ((436, 441), (96, 96)),
    ((442, 442), (97, 97)),
    ((443, 448), (98, 98)),
    ((449, 454), (99, 99)),
    ((455, 460), (100, 100)),
    ((461, 461), (101, 101)),
    ((474, 478), (104, 104)),
    ((480, 485), (106, 106)),
    ((486, 486), (107, 107)),
    ((487, 492), (108, 108)),
    ((493, 498), (109, 109)),
    ((499, 504), (110, 110)),
    ((505, 505), (111, 111)),
    ((518, 522), (114, 114)),
    ((524, 529), (116, 116)),
    ((530, 530), (117, 117)),
    ((531, 536), (118, 118)),
    ((537, 542), (119, 119)),
    ((543, 548), (120, 120)),
    ((549, 554), (121, 121)),
    ((555, 555), (122, 122)),
    ((556, 561), (123, 123)),
    ((574, 578), (127, 127)),
    ((580, 585), (129, 129)),
    ((586, 586), (130, 130)),
    ((587, 592), (131, 131)),
    ((593, 598), (132, 132)),
    ((599, 604), (133, 133)),
    ((605, 610), (134, 134)),
    ((611, 611), (135, 135)),
    ((624, 628), (138, 138)),
    ((630, 635), (140, 140)),
    ((636, 636), (141, 141)),
    ((637, 642), (142, 142)),
    ((643, 648), (143, 143)),
    ((649, 654), (144, 144)),
    ((655, 660), (145, 145)),
    ((661, 661), (146, 146)),
    ((662, 667), (147, 147)),
)
