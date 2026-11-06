---
type: smite-build
god: Thor
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thunderstruck
  aspect_pick_rate: 0.29
  aspect_win_rate: 0.54
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.53
    win_rate: 0.49
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.47
    - name: Devourer's Gauntlet
      pick_rate: 0.08
      win_rate: 0.55
  - name: Hydra's Lament
    pick_rate: 0.27
    win_rate: 0.48
    alternates:
    - name: Barbed Carver
      pick_rate: 0.12
      win_rate: 0.37
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.54
  - name: Barbed Carver
    pick_rate: 0.11
    win_rate: 0.41
    alternates:
    - name: The Crusher
      pick_rate: 0.11
      win_rate: 0.52
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.69
  - name: Heartseeker
    pick_rate: 0.32
    win_rate: 0.49
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.57
    - name: The Crusher
      pick_rate: 0.07
      win_rate: 0.5
  - name: Titan's Bane
    pick_rate: 0.14
    win_rate: 0.63
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.67
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.19
  - name: Skeggox
    pick_rate: 0.1
    win_rate: 0.4
    alternates:
    - name: Avatar's Parashu
      pick_rate: 0.06
      win_rate: 0.78
    - name: Magi's Cloak
      pick_rate: 0.05
      win_rate: 0.63
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.38
    win_rate: 0.49
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.64
  - name: Bumba's Cudgel
    pick_rate: 0.18
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/thor/
  last_verified: '2026-11-06'
  god_win_rate: 0.5121107266435986
  god_matches_won: 148
  god_matches_played: 289
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, The Reaper, Shield Splitter, Genji''s
    Guard, Berserker''s Shield, Runeforged Hammer, Oni Hunter''s Garb, Shield of the
    Phoenix, Breastplate of Valor, Draconic Scale, Tyrfing, Avenging Blade, Erosion,
    Eye of Providence, Midgardian Mail, Wyrmskin Hide, Golden Blade, Leviathan''s
    Hide, Arondight, Hide of the Nemean Lion, Sanguine Lash, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.49
      pick: 0.53
      fit: 0.49
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.69
      pick: 0.16
      fit: 0.27
    Titan's Bane:
      total: 0.55
      efficiency: 0.48
      win: 0.63
      pick: 0.3
      fit: 0.55
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.46
      win: 0.78
      pick: 0.18
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Genji's Guard
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Amanita Charm, Kinetic Cuirass, The Reaper, Breastplate of Valor, Berserker''s
    Shield, Shield Splitter, Runeforged Hammer, Oni Hunter''s Garb, Shield of the
    Phoenix, Tyrfing, Arondight, Screeching Gargoyle, Avenging Blade, Draconic Scale,
    Yogi''s Necklace, Midgardian Mail, Erosion, Leviathan''s Hide, Eye of Providence,
    Transcendence, Hide of the Nemean Lion, Chandra''s Grace, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.49
      pick: 0.53
      fit: 0.49
    Transcendence:
      total: 0.44
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.27
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.69
      pick: 0.16
      fit: 0.24
    Titan's Bane:
      total: 0.53
      efficiency: 0.48
      win: 0.63
      pick: 0.3
      fit: 0.42
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.46
      win: 0.78
      pick: 0.18
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Genji''s Guard, Amanita Charm, The Reaper, Kinetic Cuirass, Berserker''s
    Shield, Breastplate of Valor, Shield of the Phoenix, Shield Splitter, Runeforged
    Hammer, Oni Hunter''s Garb, Screeching Gargoyle, Arondight, Draconic Scale, Tyrfing,
    Midgardian Mail, Avenging Blade, Erosion, Leviathan''s Hide, Pendulum Blade, Eye
    of Providence, Hide of the Nemean Lion, Gladiator''s Shield, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.49
      pick: 0.53
      fit: 0.52
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.69
      pick: 0.16
      fit: 0.3
    Titan's Bane:
      total: 0.54
      efficiency: 0.48
      win: 0.63
      pick: 0.3
      fit: 0.47
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.46
      win: 0.78
      pick: 0.18
      fit: 0.37
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.25
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - The Reaper
  - Titan's Bane
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Titan's Bane
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, Shield Splitter, Genji''s Guard, Phoenix Feather, Yogi''s Necklace, Runeforged
    Hammer, Draconic Scale, Oni Hunter''s Garb, Erosion, Bloodforge, Eye of Providence,
    Breastplate of Valor, Chandra''s Grace, Midgardian Mail, Leviathan''s Hide, Avenging
    Blade, Hide of the Nemean Lion, Wyrmskin Hide, Shifter''s Shield, Regrowth Striders.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.49
      pick: 0.53
      fit: 0.4
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.69
      pick: 0.16
      fit: 0.34
    The Reaper:
      total: 0.54
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.77
    Titan's Bane:
      total: 0.54
      efficiency: 0.48
      win: 0.63
      pick: 0.3
      fit: 0.47
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.46
      win: 0.78
      pick: 0.18
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - The Reaper
  - Titan's Bane
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - The Reaper
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Amanita Charm, Avenging Blade, Kinetic Cuirass, Genji''s
    Guard, Screeching Gargoyle, Berserker''s Shield, Stone of Binding, Shield Splitter,
    Void Stone, Runeforged Hammer, Void Shield, Breastplate of Valor, Oni Hunter''s
    Garb, Shield of the Phoenix, Tekko-Kagi, Tyrfing, Draconic Scale, Pendulum Blade,
    Midgardian Mail, Erosion, Eye of Providence, Toxic Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.49
      pick: 0.53
      fit: 0.6
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.69
      pick: 0.16
      fit: 0.21
    The Reaper:
      total: 0.53
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.66
    Titan's Bane:
      total: 0.57
      efficiency: 0.48
      win: 0.63
      pick: 0.3
      fit: 0.67
    Heartseeker:
      total: 0.52
      efficiency: 0.45
      win: 0.49
      pick: 0.53
      fit: 0.77
    Avatar's Parashu:
      total: 0.61
      efficiency: 0.46
      win: 0.78
      pick: 0.18
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Tyrfing, Amanita Charm, Golden Blade, Kinetic Cuirass,
    Genji''s Guard, Toxic Blade, The Reaper, Silverbranch Bow, Shield Splitter, Riptalon,
    Tekko-Kagi, Runeforged Hammer, Breastplate of Valor, Oni Hunter''s Garb, Lernaean
    Bow, Dominance, Shogun''s Ofuda, Pharaoh''s Curse, Shield of the Phoenix, Qin''s
    Blade, Draconic Scale, Midgardian Mail, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.42
    Tyrfing:
      total: 0.51
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.69
      pick: 0.16
      fit: 0.18
    Titan's Bane:
      total: 0.52
      efficiency: 0.48
      win: 0.63
      pick: 0.3
      fit: 0.35
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.46
      win: 0.78
      pick: 0.18
      fit: 0.25
  community_ordered:
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Breastplate of Valor
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Titan's Bane
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Screeching Gargoyle, Berserker''s
    Shield, Arondight, The Reaper, Gladiator''s Shield, Shield Splitter, Runeforged
    Hammer, Oni Hunter''s Garb, Chandra''s Grace, Prophetic Cloak, Eye of Erebus,
    Draconic Scale, Damaru, Regrowth Striders, Midgardian Mail, Erosion, Pendulum
    Blade, Leviathan''s Hide, Eye of Providence, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.49
      pick: 0.53
      fit: 0.55
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.69
      pick: 0.16
      fit: 0.48
    Titan's Bane:
      total: 0.51
      efficiency: 0.48
      win: 0.63
      pick: 0.3
      fit: 0.33
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.46
      win: 0.78
      pick: 0.18
      fit: 0.23
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, The Reaper, Shield Splitter,
    Genji''s Guard, Berserker''s Shield, Runeforged Hammer, Oni Hunter''s Garb, Shield
    of the Phoenix, Breastplate of Valor, Draconic Scale, Tyrfing, Avenging Blade,
    Erosion, Eye of Providence, Midgardian Mail, Wyrmskin Hide, Shifter''s Shield,
    Golden Blade, Leviathan''s Hide, Arondight, Hide of the Nemean Lion, Sanguine
    Lash.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.16
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.49
      pick: 0.53
      fit: 0.49
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.49
    Shield Splitter:
      total: 0.5
      efficiency: 0.58
      win: 0.51
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
