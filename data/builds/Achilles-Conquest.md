---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.62
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.19
    win_rate: 0.54
    alternates:
    - name: Avenging Blade
      pick_rate: 0.17
      win_rate: 0.53
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.52
  - name: Shifter's Shield
    pick_rate: 0.14
    win_rate: 0.55
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.09
      win_rate: 0.52
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.58
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.57
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.54
  - name: Brawler’s Beat Stick
    pick_rate: 0.08
    win_rate: 0.44
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.51
    - name: Gladiator's Shield
      pick_rate: 0.07
      win_rate: 0.52
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.6
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.6
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.57
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.09
      win_rate: 0.6
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.79
  community_starters:
  - name: Sundering Axe
    pick_rate: 0.19
    win_rate: 0.69
  - name: Hunter's Cowl
    pick_rate: 0.14
    win_rate: 0.53
  - name: Bluestone Brooch
    pick_rate: 0.13
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-10-30'
  god_win_rate: 0.5441176470588235
  god_matches_won: 185
  god_matches_played: 340
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer, Kinetic Cuirass,
    Hydra''s Lament, Eye of the Storm, Shield Splitter, Heartseeker, Berserker''s
    Shield, Genji''s Guard, Breastplate of Valor, Titan''s Bane, The Crusher, Erosion,
    The Reaper, Eye of Providence, Draconic Scale, Shield of the Phoenix, Golden Blade,
    Daybreak Gavel, Midgardian Mail, Avatar''s Parashu, Stone of Binding, Leviathan''s
    Hide, Void Shield, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.11
      fit: 0.56
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.58
      pick: 0.11
      fit: 0.44
    Hide of the Nemean Lion:
      total: 0.52
      efficiency: 0.52
      win: 0.63
      pick: 0.15
      fit: 0.33
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Kinetic Cuirass
  - Hydra's Lament
  - Hide of the Nemean Lion
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, Amanita Charm, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Heartseeker, Kinetic Cuirass, Shield Splitter, Eye of the Storm,
    Berserker''s Shield, Titan''s Bane, The Crusher, Shield of the Phoenix, Transcendence,
    Daybreak Gavel, The Reaper, Arondight, Screeching Gargoyle, Erosion, Eye of Providence,
    Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian
    Mail, Golden Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.52
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.28
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.11
      fit: 0.49
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.56
      pick: 0.17
      fit: 0.25
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Hydra's Lament
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix,
    Runeforged Hammer, The Reaper, Shield Splitter, Eye of the Storm, Hydra''s Lament,
    Berserker''s Shield, Erosion, Genji''s Guard, Eye of Providence, Breastplate of
    Valor, Yogi''s Necklace, Draconic Scale, Phoenix Feather, Heartseeker, Stone of
    Binding, Midgardian Mail, Titan''s Bane, Chandra''s Grace, The Crusher, Daybreak
    Gavel, Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.11
      fit: 0.65
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.72
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.19
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.17
      fit: 0.38
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Titan's Bane
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Heartseeker, Amanita Charm, Titan''s Bane, The
    Crusher, Runeforged Hammer, Kinetic Cuirass, Stone of Binding, The Reaper, Hydra''s
    Lament, Void Shield, Screeching Gargoyle, Void Stone, Shield Splitter, Eye of
    the Storm, Avatar''s Parashu, Genji''s Guard, Berserker''s Shield, Breastplate
    of Valor, Pendulum Blade, Tekko-Kagi, Erosion, Daybreak Gavel, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Toxic Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.53
      pick: 0.17
      fit: 0.78
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.65
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.22
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.55
      pick: 0.0
      fit: 0.81
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.55
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Avenging Blade
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Golden Blade, Amanita Charm,
    Riptalon, Tyrfing, Silverbranch Bow, Kinetic Cuirass, Toxic Blade, Runeforged
    Hammer, Hydra''s Lament, Lernaean Bow, Genji''s Guard, Breastplate of Valor, Pharaoh''s
    Curse, Tekko-Kagi, The Reaper, Shogun''s Ofuda, Shield Splitter, Heartseeker,
    Eye of the Storm, Daybreak Gavel, Dominance, Erosion, Shield of the Phoenix, Eye
    of Providence, Qin''s Blade.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.27
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.55
      pick: 0.0
      fit: 0.6
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Breastplate of Valor
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Hydra''s Lament, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Kinetic
    Cuirass, Screeching Gargoyle, Runeforged Hammer, Berserker''s Shield, Arondight,
    Eye of Erebus, Pendulum Blade, Shield Splitter, Gladiator''s Shield, Prophetic
    Cloak, Chandra''s Grace, Heartseeker, Eye of the Storm, Daybreak Gavel, Erosion,
    Eye of Providence, Draconic Scale, Midgardian Mail, Stone of Binding, Titan''s
    Bane, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.59
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.1
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.11
      fit: 0.55
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.17
      fit: 0.52
  community_ordered:
  - Hydra's Lament
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Eye of the Storm
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Eye of the Storm
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Eye of the Storm, Shield Splitter, Heartseeker, Berserker''s
    Shield, Genji''s Guard, Hydra''s Lament, Breastplate of Valor, Titan''s Bane,
    The Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale, Shield of
    the Phoenix, Golden Blade, Daybreak Gavel, Midgardian Mail, Avatar''s Parashu,
    Stone of Binding, Leviathan''s Hide, Void Shield, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.11
      fit: 0.56
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.54
    Eye of the Storm:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.62
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
