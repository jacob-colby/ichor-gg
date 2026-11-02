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
      win_rate: 0.44
    - name: Transcendence
      pick_rate: 0.05
      win_rate: 0.51
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
      win_rate: 0.54
    - name: Sanguine Lash
      pick_rate: 0.09
      win_rate: 0.45
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.49
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.48
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.54
  - name: Heartseeker
    pick_rate: 0.05
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.63
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.52
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
    win_rate: 0.39
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-11-02'
  god_win_rate: 0.4761421319796954
  god_matches_won: 469
  god_matches_played: 985
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Heartseeker, Amanita Charm, Genji''s Guard, Runeforged Hammer, Shield
    Splitter, Titan''s Bane, Hydra''s Lament, Berserker''s Shield, Breastplate of
    Valor, The Crusher, Avenging Blade, Shield of the Phoenix, Oni Hunter''s Garb,
    The Reaper, Erosion, Wyrmskin Hide, Arondight, Eye of Providence, Midgardian Mail,
    Draconic Scale, Leviathan''s Hide, Screeching Gargoyle, Tekko-Kagi, Pendulum Blade,
    Golden Blade, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.44
      pick: 0.19
      fit: 0.58
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.2
      fit: 0.52
    Transcendence:
      total: 0.44
      efficiency: 0.49
      win: 0.51
      pick: 0.05
      fit: 0.27
    Heartseeker:
      total: 0.52
      efficiency: 0.41
      win: 0.6
      pick: 0.11
      fit: 0.65
    Amanita Charm:
      total: 0.51
      efficiency: 0.62
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Genji''s Guard, Amanita Charm, Hydra''s Lament, Breastplate of Valor, Runeforged
    Hammer, Titan''s Bane, Shield Splitter, Berserker''s Shield, Oni Hunter''s Garb,
    The Crusher, Avenging Blade, Arondight, Shield of the Phoenix, The Reaper, Transcendence,
    Screeching Gargoyle, Midgardian Mail, Yogi''s Necklace, Erosion, Leviathan''s
    Hide, Tekko-Kagi, Wyrmskin Hide, Eye of Providence, Draconic Scale, Chandra''s
    Grace, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.44
      pick: 0.19
      fit: 0.52
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.58
      pick: 0.2
      fit: 0.37
    Transcendence:
      total: 0.45
      efficiency: 0.49
      win: 0.51
      pick: 0.05
      fit: 0.28
    Heartseeker:
      total: 0.51
      efficiency: 0.41
      win: 0.6
      pick: 0.11
      fit: 0.62
    Amanita Charm:
      total: 0.49
      efficiency: 0.62
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    god: Heartseeker, Genji''s Guard, Amanita Charm, Titan''s Bane, Breastplate of
    Valor, Hydra''s Lament, Runeforged Hammer, Shield Splitter, Berserker''s Shield,
    The Crusher, Shield of the Phoenix, The Reaper, Screeching Gargoyle, Arondight,
    Oni Hunter''s Garb, Pendulum Blade, Tekko-Kagi, Avenging Blade, Midgardian Mail,
    Erosion, Leviathan''s Hide, Eye of Providence, Draconic Scale, Stone of Binding,
    Chandra''s Grace, Ancile, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.44
      pick: 0.19
      fit: 0.56
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.58
      pick: 0.2
      fit: 0.39
    Transcendence:
      total: 0.43
      efficiency: 0.49
      win: 0.51
      pick: 0.05
      fit: 0.16
    Heartseeker:
      total: 0.51
      efficiency: 0.41
      win: 0.6
      pick: 0.11
      fit: 0.6
    Amanita Charm:
      total: 0.49
      efficiency: 0.62
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Heartseeker, Shield Splitter,
    Genji''s Guard, The Reaper, Runeforged Hammer, Phoenix Feather, Berserker''s Shield,
    Yogi''s Necklace, Breastplate of Valor, Titan''s Bane, Chandra''s Grace, Erosion,
    Hydra''s Lament, Eye of Providence, Oni Hunter''s Garb, Draconic Scale, Midgardian
    Mail, Avenging Blade, Glorious Pridwen, Wyrmskin Hide, Regrowth Striders, Leviathan''s
    Hide, The Crusher, Stone of Binding.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.44
      pick: 0.19
      fit: 0.49
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.2
      fit: 0.61
    Shield Splitter:
      total: 0.5
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.54
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.49
      win: 0.51
      pick: 0.0
      fit: 0.76
    Heartseeker:
      total: 0.51
      efficiency: 0.41
      win: 0.6
      pick: 0.11
      fit: 0.58
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
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
  - Titan's Bane
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Heartseeker, Titan''s Bane, Avenging Blade, Amanita Charm, Screeching
    Gargoyle, The Crusher, Genji''s Guard, Stone of Binding, The Reaper, Runeforged
    Hammer, Void Stone, Shield Splitter, Void Shield, Hydra''s Lament, Berserker''s
    Shield, Breastplate of Valor, Tekko-Kagi, Pendulum Blade, Oni Hunter''s Garb,
    Avatar''s Parashu, Shield of the Phoenix, Midgardian Mail, Erosion, Arondight,
    Toxic Blade, Eye of Providence, Draconic Scale.'
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.45
      win: 0.51
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.44
      pick: 0.19
      fit: 0.67
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.53
      win: 0.58
      pick: 0.2
      fit: 0.43
    Titan's Bane:
      total: 0.51
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.54
      efficiency: 0.41
      win: 0.6
      pick: 0.11
      fit: 0.77
    Amanita Charm:
      total: 0.5
      efficiency: 0.62
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
  - Toxic Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Toxic Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Amanita Charm, Heartseeker, Genji''s
    Guard, Toxic Blade, Tekko-Kagi, Tyrfing, Silverbranch Bow, Riptalon, Breastplate
    of Valor, Runeforged Hammer, Lernaean Bow, The Reaper, Pharaoh''s Curse, Shield
    Splitter, Titan''s Bane, Hydra''s Lament, Shogun''s Ofuda, Oni Hunter''s Garb,
    Dominance, Shield of the Phoenix, Midgardian Mail, Qin''s Blade, Screeching Gargoyle,
    The Crusher, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.49
      win: 0.51
      pick: 0.0
      fit: 0.59
    Toxic Blade:
      total: 0.48
      efficiency: 0.46
      win: 0.51
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.52
      efficiency: 0.7
      win: 0.46
      pick: 0.14
      fit: 0.4
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.58
      pick: 0.2
      fit: 0.36
    Heartseeker:
      total: 0.48
      efficiency: 0.41
      win: 0.6
      pick: 0.11
      fit: 0.43
    Amanita Charm:
      total: 0.49
      efficiency: 0.62
      win: 0.51
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Heartseeker
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
  - Freya's Tears
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Heartseeker, Screeching
    Gargoyle, Arondight, Berserker''s Shield, Runeforged Hammer, Chandra''s Grace,
    Shield Splitter, Titan''s Bane, Gladiator''s Shield, Prophetic Cloak, Pendulum
    Blade, Eye of Erebus, Oni Hunter''s Garb, Midgardian Mail, Erosion, Regrowth Striders,
    Eye of Providence, Leviathan''s Hide, Draconic Scale, The Crusher, Damaru, Avenging
    Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.61
      win: 0.51
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.44
      pick: 0.19
      fit: 0.59
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.53
      win: 0.58
      pick: 0.2
      fit: 0.41
    Freya's Tears:
      total: 0.5
      efficiency: 0.55
      win: 0.49
      pick: 0.28
      fit: 0.52
    Amanita Charm:
      total: 0.49
      efficiency: 0.62
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
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Berserker''s Shield, Genji''s Guard, Runeforged
    Hammer, Shield Splitter, Titan''s Bane, Hydra''s Lament, Breastplate of Valor,
    Heartseeker, The Crusher, Avenging Blade, Shield of the Phoenix, Oni Hunter''s
    Garb, The Reaper, Erosion, Wyrmskin Hide, Arondight, Eye of Providence, Midgardian
    Mail, Draconic Scale, Leviathan''s Hide, Screeching Gargoyle, Tekko-Kagi, Pendulum
    Blade, Golden Blade, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.48
      efficiency: 0.63
      win: 0.46
      pick: 0.14
      fit: 0.31
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.44
      pick: 0.19
      fit: 0.58
    Shield Splitter:
      total: 0.49
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.49
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.51
      efficiency: 0.62
      win: 0.51
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Sanguine Lash
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Sanguine Lash
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Berserker''s Shield,
    Genji''s Guard, Runeforged Hammer, Shield Splitter, Titan''s Bane, Hydra''s Lament,
    Breastplate of Valor, Heartseeker, The Crusher, Avenging Blade, Shield of the
    Phoenix, Oni Hunter''s Garb, The Reaper, Erosion, Wyrmskin Hide, Arondight, Eye
    of Providence, Midgardian Mail, Draconic Scale, Leviathan''s Hide, Screeching
    Gargoyle, Tekko-Kagi, Pendulum Blade, Golden Blade, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.48
      efficiency: 0.63
      win: 0.46
      pick: 0.14
      fit: 0.31
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.44
      pick: 0.19
      fit: 0.58
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.2
      fit: 0.52
    Sanguine Lash:
      total: 0.46
      efficiency: 0.34
      win: 0.56
      pick: 0.33
      fit: 0.48
    Titan's Bane:
      total: 0.49
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Sanguine Lash
  swaps:
  - added: Sanguine Lash
    removed: Shield Splitter
    reason: community 56% win over 236 matches (vs 48% on this god), taking the model's
      weakest slot from Shield Splitter
  - added: Kinetic Cuirass
    removed: Runeforged Hammer
    reason: community 58% win over 128 matches (vs 48% on this god), taking the model's
      weakest slot from Runeforged Hammer
  starter: *id001
---
