---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.47
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.58
    win_rate: 0.51
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.19
      win_rate: 0.45
    - name: Transcendence
      pick_rate: 0.05
      win_rate: 0.52
  - name: Sanguine Lash
    pick_rate: 0.24
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.46
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.46
  - name: Kinetic Cuirass
    pick_rate: 0.13
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.55
    - name: Sanguine Lash
      pick_rate: 0.09
      win_rate: 0.45
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.49
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.47
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.54
  - name: Heartseeker
    pick_rate: 0.05
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.63
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.55
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.53
    alternates:
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.48
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.41
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.56
  - name: Hunter's Cowl
    pick_rate: 0.24
    win_rate: 0.56
  - name: Leather Cowl
    pick_rate: 0.15
    win_rate: 0.38
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-11-04'
  god_win_rate: 0.47847847847847846
  god_matches_won: 478
  god_matches_played: 999
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Heartseeker, Genji''s Guard, Shield Splitter, Runeforged
    Hammer, Hydra''s Lament, Shield of the Phoenix, The Crusher, Berserker''s Shield,
    Breastplate of Valor, Oni Hunter''s Garb, Titan''s Bane, Draconic Scale, The Reaper,
    Avenging Blade, Arondight, Erosion, Eye of Providence, Wyrmskin Hide, Midgardian
    Mail, Tyrfing, Screeching Gargoyle, Leviathan''s Hide, Golden Blade, Gladiator''s
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.45
      pick: 0.19
      fit: 0.58
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.2
      fit: 0.52
    Transcendence:
      total: 0.45
      efficiency: 0.5
      win: 0.52
      pick: 0.05
      fit: 0.27
    Heartseeker:
      total: 0.53
      efficiency: 0.45
      win: 0.59
      pick: 0.11
      fit: 0.65
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Heartseeker,
    Genji''s Guard, Amanita Charm, Hydra''s Lament, Breastplate of Valor, Shield Splitter,
    Runeforged Hammer, Oni Hunter''s Garb, The Crusher, Shield of the Phoenix, Berserker''s
    Shield, Titan''s Bane, The Reaper, Arondight, Avenging Blade, Tyrfing, Screeching
    Gargoyle, Draconic Scale, Yogi''s Necklace, Transcendence, Midgardian Mail, Erosion,
    Leviathan''s Hide, Eye of Providence, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.45
      pick: 0.19
      fit: 0.52
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.2
      fit: 0.37
    Transcendence:
      total: 0.45
      efficiency: 0.5
      win: 0.52
      pick: 0.05
      fit: 0.28
    Heartseeker:
      total: 0.52
      efficiency: 0.45
      win: 0.59
      pick: 0.11
      fit: 0.62
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Heartseeker, Genji''s Guard, Amanita Charm, Breastplate of Valor, Hydra''s
    Lament, Shield of the Phoenix, The Crusher, Shield Splitter, Runeforged Hammer,
    Berserker''s Shield, Titan''s Bane, The Reaper, Oni Hunter''s Garb, Screeching
    Gargoyle, Arondight, Draconic Scale, Midgardian Mail, Avenging Blade, Erosion,
    Pendulum Blade, Leviathan''s Hide, Eye of Providence, Tyrfing, Avatar''s Parashu,
    Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.45
      pick: 0.19
      fit: 0.56
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.2
      fit: 0.39
    Transcendence:
      total: 0.43
      efficiency: 0.5
      win: 0.52
      pick: 0.05
      fit: 0.16
    Heartseeker:
      total: 0.52
      efficiency: 0.45
      win: 0.59
      pick: 0.11
      fit: 0.6
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Genji''s Guard, Heartseeker, Shield
    Splitter, The Reaper, Phoenix Feather, Yogi''s Necklace, Runeforged Hammer, Berserker''s
    Shield, Draconic Scale, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s
    Garb, Hydra''s Lament, Erosion, Eye of Providence, The Crusher, Midgardian Mail,
    Regrowth Striders, Leviathan''s Hide, Avenging Blade, Glorious Pridwen, Wyrmskin
    Hide, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.45
      pick: 0.19
      fit: 0.49
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.2
      fit: 0.61
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.76
    Heartseeker:
      total: 0.52
      efficiency: 0.45
      win: 0.59
      pick: 0.11
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Heartseeker, Amanita Charm, The Crusher, Avenging Blade, Genji''s
    Guard, Screeching Gargoyle, Titan''s Bane, The Reaper, Shield Splitter, Stone
    of Binding, Void Stone, Runeforged Hammer, Void Shield, Hydra''s Lament, Berserker''s
    Shield, Breastplate of Valor, Shield of the Phoenix, Avatar''s Parashu, Oni Hunter''s
    Garb, Pendulum Blade, Draconic Scale, Tekko-Kagi, Arondight, Midgardian Mail,
    Erosion, Tyrfing, Eye of Providence.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.47
      win: 0.51
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.45
      pick: 0.19
      fit: 0.67
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.2
      fit: 0.43
    The Crusher:
      total: 0.51
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.59
      pick: 0.11
      fit: 0.77
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Tyrfing, Genji''s Guard, Golden
    Blade, Heartseeker, Toxic Blade, The Reaper, Breastplate of Valor, Silverbranch
    Bow, Shield Splitter, Runeforged Hammer, Shield of the Phoenix, Tekko-Kagi, Riptalon,
    Hydra''s Lament, Oni Hunter''s Garb, Shogun''s Ofuda, Lernaean Bow, Pharaoh''s
    Curse, Dominance, The Crusher, Draconic Scale, Midgardian Mail, Screeching Gargoyle,
    Qin''s Blade, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.59
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.15
    Berserker's Shield:
      total: 0.53
      efficiency: 0.72
      win: 0.46
      pick: 0.14
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.2
      fit: 0.36
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Shield of the Phoenix, Hydra''s Lament, Heartseeker, Screeching
    Gargoyle, Arondight, Gladiator''s Shield, Berserker''s Shield, Shield Splitter,
    Chandra''s Grace, Runeforged Hammer, Oni Hunter''s Garb, Eye of Erebus, Prophetic
    Cloak, Draconic Scale, Damaru, The Crusher, Midgardian Mail, Regrowth Striders,
    Erosion, Pendulum Blade, Eye of Providence, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.45
      pick: 0.19
      fit: 0.59
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.2
      fit: 0.41
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.49
      pick: 0.28
      fit: 0.52
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Shield Splitter
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
    Underrated for this god: Amanita Charm, Genji''s Guard, Shield Splitter, Berserker''s
    Shield, Runeforged Hammer, Hydra''s Lament, Shield of the Phoenix, The Crusher,
    Breastplate of Valor, Heartseeker, Oni Hunter''s Garb, Titan''s Bane, Draconic
    Scale, The Reaper, Avenging Blade, Arondight, Erosion, Eye of Providence, Wyrmskin
    Hide, Midgardian Mail, Tyrfing, Screeching Gargoyle, Leviathan''s Hide, Golden
    Blade, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.49
      efficiency: 0.66
      win: 0.46
      pick: 0.14
      fit: 0.31
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.45
      pick: 0.19
      fit: 0.58
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.2
      fit: 0.52
    Shield Splitter:
      total: 0.51
      efficiency: 0.58
      win: 0.51
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Sanguine Lash
  - Runeforged Hammer
  flex_slots:
  - Runeforged Hammer
  - Sanguine Lash
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Genji''s Guard, Shield
    Splitter, Berserker''s Shield, Runeforged Hammer, Hydra''s Lament, Shield of the
    Phoenix, The Crusher, Breastplate of Valor, Heartseeker, Oni Hunter''s Garb, Titan''s
    Bane, Draconic Scale, The Reaper, Avenging Blade, Arondight, Erosion, Eye of Providence,
    Wyrmskin Hide, Midgardian Mail, Tyrfing, Screeching Gargoyle, Leviathan''s Hide,
    Golden Blade, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.51
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.45
      pick: 0.19
      fit: 0.58
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.2
      fit: 0.52
    Shield Splitter:
      total: 0.51
      efficiency: 0.58
      win: 0.51
      pick: 0.0
      fit: 0.5
    Sanguine Lash:
      total: 0.47
      efficiency: 0.36
      win: 0.56
      pick: 0.33
      fit: 0.48
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Sanguine Lash
  swaps:
  - added: Sanguine Lash
    removed: Berserker's Shield
    reason: community 56% win over 240 matches (vs 48% on this god), taking the model's
      weakest slot from Berserker's Shield
  starter: *id001
---
