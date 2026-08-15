---
type: smite-build
god: Anhur
mode: Conquest
builds:
- source: community
  aspect: Aspect of Pride
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.62
  slot_order:
  - name: Tyrfing
    pick_rate: 0.57
    win_rate: 0.54
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.15
      win_rate: 0.51
    - name: Avenging Blade
      pick_rate: 0.11
      win_rate: 0.42
  - name: Odysseus' Bow
    pick_rate: 0.31
    win_rate: 0.51
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.19
      win_rate: 0.47
    - name: Toxic Blade
      pick_rate: 0.11
      win_rate: 0.37
  - name: The Executioner
    pick_rate: 0.15
    win_rate: 0.66
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.42
    - name: Silverbranch Bow
      pick_rate: 0.13
      win_rate: 0.49
  - name: Silverbranch Bow
    pick_rate: 0.23
    win_rate: 0.65
    alternates:
    - name: The Executioner
      pick_rate: 0.2
      win_rate: 0.37
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.48
  - name: Riptalon
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.19
      win_rate: 0.54
    - name: The Executioner
      pick_rate: 0.14
      win_rate: 0.64
  - name: Manchu Bow
    pick_rate: 0.12
    win_rate: 0.44
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.11
      win_rate: 0.64
    - name: Qin's Blade
      pick_rate: 0.09
      win_rate: 0.37
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.31
    win_rate: 0.52
  - name: Sharpshooter's Arrow
    pick_rate: 0.28
    win_rate: 0.52
  - name: Gilded Arrow
    pick_rate: 0.14
    win_rate: 0.41
  source_url: https://smitebrain.com/gods/anhur/
  last_verified: '2026-08-15'
  god_win_rate: 0.4968944099378882
  god_matches_won: 160
  god_matches_played: 322
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-15'
  god_matches_analyzed: 4746
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Damaru
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Damaru, Berserker''s Shield, Jotunn''s Revenge, Lernaean
    Bow, Golden Blade, Genji''s Guard, Hydra''s Lament, Demon Blade, Dominance, Runeforged
    Hammer, The Reaper, Tekko-Kagi, Pharaoh''s Curse, Deathbringer, Breastplate of
    Valor, Kinetic Cuirass, Musashi''s Dual Swords, Shogun''s Ofuda, Amanita Charm,
    Eye of Providence, Oni Hunter''s Garb, Transcendence, Rage, Freya''s Tears, Avenging
    Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.29
    Tyrfing:
      total: 0.52
      efficiency: 0.46
      win: 0.54
      pick: 0.57
      fit: 0.6
    Riptalon:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.3
      fit: 0.46
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.65
      pick: 0.38
      fit: 0.35
    Damaru:
      total: 0.5
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.36
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, The Crusher, Genji''s Guard, Hydra''s Lament, Berserker''s Shield, Damaru,
    Breastplate of Valor, Lernaean Bow, Golden Blade, The Reaper, Runeforged Hammer,
    Dominance, Oni Hunter''s Garb, Tekko-Kagi, Kinetic Cuirass, Amanita Charm, Freya''s
    Tears, Transcendence, Pharaoh''s Curse, Eye of Providence, Heartseeker, Shield
    of the Phoenix, Yogi''s Necklace, Deathbringer, Arondight, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.15
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.5
      efficiency: 0.46
      win: 0.54
      pick: 0.57
      fit: 0.44
    Hydra's Lament:
      total: 0.49
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.42
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.65
      pick: 0.38
      fit: 0.28
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Silverbranch Bow
  - Damaru
  - Demon Blade
  - The Crusher
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Damaru, The Crusher, Berserker''s Shield, Jotunn''s Revenge, Lernaean
    Bow, Golden Blade, Genji''s Guard, Hydra''s Lament, Demon Blade, Runeforged Hammer,
    The Reaper, Deathbringer, Dominance, Pharaoh''s Curse, Tekko-Kagi, Breastplate
    of Valor, Musashi''s Dual Swords, Kinetic Cuirass, Amanita Charm, Shogun''s Ofuda,
    Eye of Providence, Rage, Oni Hunter''s Garb, Freya''s Tears, Transcendence, Avenging
    Blade.'
  slot_scores:
    Tyrfing:
      total: 0.51
      efficiency: 0.46
      win: 0.54
      pick: 0.57
      fit: 0.55
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.65
      pick: 0.38
      fit: 0.33
    Damaru:
      total: 0.5
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.52
    Demon Blade:
      total: 0.47
      efficiency: 0.35
      win: 0.51
      pick: 0.0
      fit: 0.79
    The Crusher:
      total: 0.5
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.34
    Deathbringer:
      total: 0.46
      efficiency: 0.45
      win: 0.51
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    The Crusher, Genji''s Guard, The Reaper, Pharaoh''s Curse, Chandra''s Grace, Golden
    Blade, Oni Hunter''s Garb, Jotunn''s Revenge, Runeforged Hammer, Damaru, Phoenix
    Feather, Breastplate of Valor, Freya''s Tears, Shogun''s Ofuda, Spectral Armor,
    Lernaean Bow, Erosion, Shifter''s Shield, Eye of the Storm, Eye of Providence,
    Hydra''s Lament, Shield Splitter, Draconic Scale, Leviathan''s Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.51
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.49
      efficiency: 0.46
      win: 0.54
      pick: 0.57
      fit: 0.42
    Riptalon:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.3
      fit: 0.59
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.65
      pick: 0.38
      fit: 0.22
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Tyrfing
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, The Reaper, Berserker''s Shield,
    Tekko-Kagi, Damaru, Genji''s Guard, Lernaean Bow, Golden Blade, Hydra''s Lament,
    Screeching Gargoyle, Heartseeker, Runeforged Hammer, Breastplate of Valor, Titan''s
    Bane, Stone of Binding, Pharaoh''s Curse, Kinetic Cuirass, Void Shield, Amanita
    Charm, Dominance, Pendulum Blade, Avenging Blade, Eye of Providence, Oni Hunter''s
    Garb.'
  slot_scores:
    Berserker's Shield:
      total: 0.49
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.21
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.5
      efficiency: 0.46
      win: 0.54
      pick: 0.57
      fit: 0.46
    Riptalon:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.3
      fit: 0.61
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.52
      win: 0.65
      pick: 0.38
      fit: 0.53
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Berserker''s Shield, The Crusher, Damaru, Jotunn''s Revenge,
    Lernaean Bow, Genji''s Guard, Hydra''s Lament, Pharaoh''s Curse, Runeforged Hammer,
    Breastplate of Valor, Dominance, The Reaper, Tekko-Kagi, Kinetic Cuirass, Demon
    Blade, Amanita Charm, Shogun''s Ofuda, Eye of Providence, Oni Hunter''s Garb,
    Deathbringer, Freya''s Tears, Eros'' Bow, Transcendence.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.27
    Tyrfing:
      total: 0.54
      efficiency: 0.46
      win: 0.54
      pick: 0.57
      fit: 0.7
    Riptalon:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.3
      fit: 0.59
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.52
      win: 0.65
      pick: 0.38
      fit: 0.5
    The Crusher:
      total: 0.49
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Silverbranch Bow
  flex_slots:
  - Breastplate of Valor
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Hydra''s Lament, Breastplate of Valor, Berserker''s Shield, The Crusher, Freya''s
    Tears, Shield of the Phoenix, Damaru, Lernaean Bow, Screeching Gargoyle, Chandra''s
    Grace, Golden Blade, Arondight, Kinetic Cuirass, Pharaoh''s Curse, Runeforged
    Hammer, Amanita Charm, Eye of Providence, Oni Hunter''s Garb, The Reaper, Dominance,
    Pendulum Blade, Shogun''s Ofuda, Gladiator''s Shield, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.43
    Tyrfing:
      total: 0.49
      efficiency: 0.46
      win: 0.54
      pick: 0.57
      fit: 0.39
    Hydra's Lament:
      total: 0.5
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.5
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.65
      pick: 0.38
      fit: 0.24
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Damaru
  - The Crusher
  flex_slots:
  - Lernaean Bow
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Damaru, Berserker''s Shield, Jotunn''s Revenge,
    Lernaean Bow, Golden Blade, Genji''s Guard, Hydra''s Lament, Demon Blade, Dominance,
    Runeforged Hammer, The Reaper, Tekko-Kagi, Pharaoh''s Curse, Deathbringer, Breastplate
    of Valor, Kinetic Cuirass, Musashi''s Dual Swords, Shogun''s Ofuda, Amanita Charm,
    Eye of Providence, Oni Hunter''s Garb, Transcendence, Avenging Blade, Rage, Freya''s
    Tears.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.5
    Lernaean Bow:
      total: 0.49
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.3
    Damaru:
      total: 0.5
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - The Executioner
  - Berserker's Shield
  - Jotunn's Revenge
  - Silverbranch Bow
  - Damaru
  - The Crusher
  flex_slots:
  - Silverbranch Bow
  - The Executioner
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: The Crusher, Damaru, Berserker''s
    Shield, Jotunn''s Revenge, Lernaean Bow, Golden Blade, Genji''s Guard, Hydra''s
    Lament, Demon Blade, Dominance, Runeforged Hammer, The Reaper, Tekko-Kagi, Pharaoh''s
    Curse, Deathbringer, Breastplate of Valor, Kinetic Cuirass, Musashi''s Dual Swords,
    Shogun''s Ofuda, Amanita Charm, Eye of Providence, Oni Hunter''s Garb, Transcendence,
    Avenging Blade, Rage, Freya''s Tears.'
  slot_scores:
    The Executioner:
      total: 0.41
      efficiency: 0.13
      win: 0.66
      pick: 0.23
      fit: 0.39
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.3
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.65
      pick: 0.38
      fit: 0.35
    Damaru:
      total: 0.5
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.36
  swaps:
  - added: Silverbranch Bow
    removed: Golden Blade
    reason: community 65% win over 74 matches (vs 50% on this god), taking the model's
      weakest slot from Golden Blade
  - added: The Executioner
    removed: Lernaean Bow
    reason: community 66% win over 48 matches (vs 50% on this god), taking the model's
      weakest slot from Lernaean Bow
  starter: *id001
---
