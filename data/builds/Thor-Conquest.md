---
type: smite-build
god: Thor
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thunderstruck
  aspect_pick_rate: 0.3
  aspect_win_rate: 0.58
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.6
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.65
    - name: Runeforged Hammer
      pick_rate: 0.07
      win_rate: 0.38
  - name: Hydra's Lament
    pick_rate: 0.27
    win_rate: 0.52
    alternates:
    - name: Barbed Carver
      pick_rate: 0.15
      win_rate: 0.44
    - name: Transcendence
      pick_rate: 0.1
      win_rate: 0.78
  - name: The Reaper
    pick_rate: 0.12
    win_rate: 0.32
    alternates:
    - name: Barbed Carver
      pick_rate: 0.11
      win_rate: 0.35
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.56
  - name: Heartseeker
    pick_rate: 0.31
    win_rate: 0.5
    alternates:
    - name: Titan's Bane
      pick_rate: 0.12
      win_rate: 0.48
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.64
  - name: Titan's Bane
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.52
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.5
  - name: Lucerne Hammer
    pick_rate: 0.08
    win_rate: 0.75
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.57
    - name: Skeggox
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.31
    win_rate: 0.63
  - name: Bumba's Cudgel
    pick_rate: 0.21
    win_rate: 0.38
  - name: Bluestone Brooch
    pick_rate: 0.2
    win_rate: 0.72
  source_url: https://smitebrain.com/gods/thor/
  last_verified: '2026-08-13'
  god_win_rate: 0.5384615384615384
  god_matches_won: 98
  god_matches_played: 182
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - The Crusher
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Shifter''s Shield, The Crusher, Kinetic Cuirass, Amanita
    Charm, Berserker''s Shield, Eye of the Storm, Oni Hunter''s Garb, Shield Splitter,
    Golden Blade, Breastplate of Valor, Avenging Blade, Freya''s Tears, Shield of
    the Phoenix, Spectral Armor, Erosion, Damaru, Lernaean Bow, Pharaoh''s Curse,
    Eye of Providence, Draconic Scale, Leviathan''s Hide, Midgardian Mail, Yogi''s
    Necklace, Runeforged Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.64
      pick: 0.1
      fit: 0.18
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.53
      pick: 0.6
      fit: 0.55
    Transcendence:
      total: 0.56
      efficiency: 0.44
      win: 0.78
      pick: 0.14
      fit: 0.3
    Hydra's Lament:
      total: 0.52
      efficiency: 0.58
      win: 0.52
      pick: 0.37
      fit: 0.44
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.65
      pick: 0.14
      fit: 0.45
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.61
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Shifter's Shield
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Genji''s Guard, The Crusher, Shifter''s Shield, Breastplate of Valor, Berserker''s
    Shield, Kinetic Cuirass, Amanita Charm, Freya''s Tears, Shield of the Phoenix,
    Oni Hunter''s Garb, Riptalon, Spectral Armor, Golden Blade, Eye of the Storm,
    Pharaoh''s Curse, Pendulum Blade, Shield Splitter, Damaru, Lernaean Bow, Silverbranch
    Bow, Chandra''s Grace, Yogi''s Necklace, Screeching Gargoyle, Avenging Blade,
    Runeforged Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.64
      pick: 0.1
      fit: 0.24
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.53
      pick: 0.6
      fit: 0.56
    Transcendence:
      total: 0.54
      efficiency: 0.44
      win: 0.78
      pick: 0.14
      fit: 0.16
    Hydra's Lament:
      total: 0.52
      efficiency: 0.58
      win: 0.52
      pick: 0.37
      fit: 0.42
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.65
      pick: 0.14
      fit: 0.27
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Transcendence
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Shifter''s Shield, Shield of the Phoenix,
    Kinetic Cuirass, The Crusher, Berserker''s Shield, Oni Hunter''s Garb, Eye of
    the Storm, Shield Splitter, Riptalon, Chandra''s Grace, Erosion, Freya''s Tears,
    Breastplate of Valor, Phoenix Feather, Eye of Providence, Spectral Armor, Pharaoh''s
    Curse, Draconic Scale, Golden Blade, Avenging Blade, Leviathan''s Hide, Midgardian
    Mail, Shogun''s Ofuda, Runeforged Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.64
      pick: 0.1
      fit: 0.21
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.53
      pick: 0.6
      fit: 0.45
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.72
    Transcendence:
      total: 0.55
      efficiency: 0.44
      win: 0.78
      pick: 0.14
      fit: 0.24
    Shifter's Shield:
      total: 0.56
      efficiency: 0.52
      win: 0.65
      pick: 0.14
      fit: 0.55
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - The Crusher
  - Heartseeker
  flex_slots:
  - Shifter's Shield
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Genji''s Guard, The Crusher, Avenging Blade, Berserker''s Shield,
    Kinetic Cuirass, Amanita Charm, Stone of Binding, Void Shield, Riptalon, Oni Hunter''s
    Garb, Screeching Gargoyle, Breastplate of Valor, Silverbranch Bow, Tekko-Kagi,
    Void Stone, Eye of the Storm, Shield Splitter, Golden Blade, Pendulum Blade, Freya''s
    Tears, Shield of the Phoenix, Spectral Armor, Damaru, Runeforged Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.64
      pick: 0.1
      fit: 0.14
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.53
      pick: 0.6
      fit: 0.66
    Transcendence:
      total: 0.55
      efficiency: 0.44
      win: 0.78
      pick: 0.14
      fit: 0.23
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.65
      pick: 0.14
      fit: 0.34
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.72
    Heartseeker:
      total: 0.52
      efficiency: 0.45
      win: 0.5
      pick: 0.52
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Riptalon
  flex_slots:
  - Riptalon
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Berserker''s Shield, Riptalon, Golden Blade, The Crusher,
    Silverbranch Bow, Pharaoh''s Curse, Kinetic Cuirass, Amanita Charm, Lernaean Bow,
    Tyrfing, Breastplate of Valor, Oni Hunter''s Garb, Shogun''s Ofuda, Toxic Blade,
    Freya''s Tears, Spectral Armor, Shield of the Phoenix, Dominance, Eros'' Bow,
    Tekko-Kagi, Yogi''s Necklace, Eye of the Storm, Damaru, Shield Splitter, Runeforged
    Hammer.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.62
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.64
      pick: 0.1
      fit: 0.1
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.6
      fit: 0.27
    Transcendence:
      total: 0.53
      efficiency: 0.44
      win: 0.78
      pick: 0.14
      fit: 0.12
    Riptalon:
      total: 0.51
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Shifter's Shield
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Shifter''s Shield, Freya''s Tears, Shield of the Phoenix, The Crusher, Berserker''s
    Shield, Kinetic Cuirass, Amanita Charm, Chandra''s Grace, Screeching Gargoyle,
    Oni Hunter''s Garb, Gladiator''s Shield, Spectral Armor, Arondight, Pendulum Blade,
    Pharaoh''s Curse, Prophetic Cloak, Erosion, Yogi''s Necklace, Eye of the Storm,
    Leviathan''s Hide, Eye of Providence, Golden Blade, Shield Splitter, Midgardian
    Mail, Runeforged Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.64
      pick: 0.1
      fit: 0.44
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.53
      pick: 0.6
      fit: 0.6
    Transcendence:
      total: 0.53
      efficiency: 0.44
      win: 0.78
      pick: 0.14
      fit: 0.11
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.52
      pick: 0.37
      fit: 0.56
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.65
      pick: 0.14
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Kinetic Cuirass, Amanita Charm, Berserker''s
    Shield, Runeforged Hammer, Genji''s Guard, Eye of the Storm, Oni Hunter''s Garb,
    Shield Splitter, Golden Blade, Breastplate of Valor, Avenging Blade, Shield of
    the Phoenix, Freya''s Tears, Spectral Armor, Shifter''s Shield, Erosion, Damaru,
    Lernaean Bow, Pharaoh''s Curse, Eye of Providence, Draconic Scale, Leviathan''s
    Hide, Midgardian Mail, Yogi''s Necklace.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.53
      pick: 0.6
      fit: 0.55
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.51
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.55
      win: 0.38
      pick: 0.07
      fit: 0.58
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.45
  starter: *id001
---
