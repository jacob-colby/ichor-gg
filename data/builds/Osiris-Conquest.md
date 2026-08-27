---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.55
  aspect_win_rate: 0.61
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.53
    win_rate: 0.59
    alternates:
    - name: Lifebinder
      pick_rate: 0.06
      win_rate: 0.67
    - name: Golden Blade
      pick_rate: 0.06
      win_rate: 0.67
  - name: Prophetic Cloak
    pick_rate: 0.22
    win_rate: 0.64
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.63
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.5
  - name: Gladiator's Shield
    pick_rate: 0.17
    win_rate: 0.63
    alternates:
    - name: Helm of Radiance
      pick_rate: 0.1
      win_rate: 0.6
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.67
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.25
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.75
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.33
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.67
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.0
  - name: Veve Charm
    pick_rate: 0.08
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.5
    - name: Draconic Scale
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Sundering Axe
    pick_rate: 0.25
    win_rate: 0.62
  - name: Warrior's Axe
    pick_rate: 0.25
    win_rate: 0.46
  - name: Death's Embrace
    pick_rate: 0.14
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-08-27'
  god_win_rate: 0.5490196078431373
  god_matches_won: 28
  god_matches_played: 51
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Jotunn''s Revenge, Amanita Charm, Runeforged Hammer, Kinetic
    Cuirass, Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm, Breastplate
    of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s Lament, Shogun''s Ofuda,
    Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic Blade, Erosion, Silverbranch
    Bow, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Midgardian Mail,
    Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.52
      win: 0.67
      pick: 0.06
      fit: 0.64
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.16
      fit: 0.45
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.3
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.47
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.59
      pick: 0.53
      fit: 0.35
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.35
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Golden Blade, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Runeforged Hammer, Shield Splitter, Eye of the Storm, Breastplate
    of Valor, The Reaper, Yogi''s Necklace, Pharaoh''s Curse, Lernaean Bow, Tyrfing,
    Riptalon, Erosion, Shogun''s Ofuda, Phoenix Feather, Eye of Providence, Avenging
    Blade, Hydra''s Lament, Chandra''s Grace, Stone of Binding, Daybreak Gavel, Midgardian
    Mail, Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.06
      fit: 0.59
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.54
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.59
      pick: 0.53
      fit: 0.44
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Golden Blade, Avenging Blade, Amanita Charm,
    Heartseeker, Tekko-Kagi, Stone of Binding, Silverbranch Bow, Runeforged Hammer,
    Screeching Gargoyle, Void Shield, Toxic Blade, Kinetic Cuirass, Titan''s Bane,
    Void Stone, The Crusher, Breastplate of Valor, Lernaean Bow, The Reaper, Tyrfing,
    Shield Splitter, Hydra''s Lament, Riptalon, Eye of the Storm, Pharaoh''s Curse,
    Avatar''s Parashu, Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.67
      pick: 0.06
      fit: 0.48
    Avenging Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.48
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.16
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.6
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Jotunn''s Revenge, Amanita Charm, Tyrfing, Kinetic Cuirass,
    Riptalon, Runeforged Hammer, Lernaean Bow, Silverbranch Bow, Breastplate of Valor,
    Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda, Shield Splitter, Eye of the Storm,
    Hydra''s Lament, Tekko-Kagi, The Reaper, Daybreak Gavel, Avenging Blade, Dominance,
    Erosion, Shield of the Phoenix, Eye of Providence, Heartseeker, Vital Amplifier,
    Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.52
      win: 0.67
      pick: 0.06
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.16
      fit: 0.41
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.18
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.59
      pick: 0.53
      fit: 0.26
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Golden Blade, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic
    Cuirass, Screeching Gargoyle, Runeforged Hammer, Arondight, Lernaean Bow, Pharaoh''s
    Curse, Tyrfing, Shield Splitter, Daybreak Gavel, Eye of Erebus, Shogun''s Ofuda,
    Eye of the Storm, Chandra''s Grace, Silverbranch Bow, Erosion, Avenging Blade,
    Eye of Providence, Stone of Binding, Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.67
      pick: 0.06
      fit: 0.39
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.4
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.26
      fit: 0.43
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Golden Blade, Runeforged
    Hammer, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm,
    Genji''s Guard, Breastplate of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s
    Lament, Shogun''s Ofuda, Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic
    Blade, Erosion, Silverbranch Bow, Daybreak Gavel, Eye of Providence, Shield of
    the Phoenix, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.52
      win: 0.67
      pick: 0.06
      fit: 0.64
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.16
      fit: 0.45
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.35
  starter: *id001
---
