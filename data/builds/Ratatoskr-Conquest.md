---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.43
  aspect_win_rate: 0.53
  slot_order:
  - name: Briskberry Acorn
    pick_rate: 0.3
    win_rate: 0.51
    alternates:
    - name: Ashwhorl Acorn
      pick_rate: 0.27
      win_rate: 0.48
    - name: Thistlethorn Acorn
      pick_rate: 0.27
      win_rate: 0.46
  - name: Thistlethorn Acorn
    pick_rate: 0.15
    win_rate: 0.6
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.41
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.59
  - name: Jotunn's Revenge
    pick_rate: 0.21
    win_rate: 0.45
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.16
      win_rate: 0.61
    - name: Briskberry Acorn
      pick_rate: 0.13
      win_rate: 0.42
  - name: Shifter's Shield
    pick_rate: 0.13
    win_rate: 0.52
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.11
      win_rate: 0.5
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.42
  - name: Titan's Bane
    pick_rate: 0.12
    win_rate: 0.52
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.5
    - name: Shield of the Phoenix
      pick_rate: 0.08
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.1
    win_rate: 0.65
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.4
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.53
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.58
  - name: Bumba's Hammer
    pick_rate: 0.2
    win_rate: 0.5
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.48
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-08-07'
  god_win_rate: 0.4936708860759494
  god_matches_won: 117
  god_matches_played: 237
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-07'
  god_matches_analyzed: 13100
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Thistlethorn Acorn, The Crusher, Genji''s Guard, The Reaper, Hydra''s
    Lament, Titan''s Bane, Runeforged Hammer, Pendulum Blade, Tekko-Kagi, Lernaean
    Bow, Avatar''s Parashu, Damaru, Heartseeker, Avenging Blade, Golden Blade, Arondight,
    Shield Splitter, Dominance, Eye of the Storm, Tyrfing, Riptalon, Silverbranch
    Bow, Berserker''s Shield, Barbed Carver, Breastplate of Valor, Transcendence,
    Bloodforge, Musashi''s Dual Swords.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.98
      win: 0.48
      pick: 0.27
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.7
      efficiency: 0.95
      win: 0.6
      pick: 0.15
      fit: 0.61
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.65
      pick: 0.1
      fit: 0.09
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.45
      pick: 0.21
      fit: 1.0
    Hydra's Lament:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.71
    The Crusher:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - The Crusher
  - Hydra's Lament
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
    god: Thistlethorn Acorn, Genji''s Guard, The Crusher, Hydra''s Lament, The Reaper,
    Pendulum Blade, Breastplate of Valor, Titan''s Bane, Runeforged Hammer, Berserker''s
    Shield, Riptalon, Tekko-Kagi, Lernaean Bow, Arondight, Damaru, Shield of the Phoenix,
    Silverbranch Bow, Freya''s Tears, Avatar''s Parashu, Amanita Charm, Oni Hunter''s
    Garb, Heartseeker, Avenging Blade, Golden Blade, Yogi''s Necklace, Kinetic Cuirass,
    Shield Splitter, Dominance.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.61
      efficiency: 0.98
      win: 0.48
      pick: 0.27
      fit: 0.22
    Thistlethorn Acorn:
      total: 0.68
      efficiency: 0.95
      win: 0.6
      pick: 0.15
      fit: 0.44
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.65
      pick: 0.1
      fit: 0.22
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.45
      pick: 0.21
      fit: 0.78
    Hydra's Lament:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Thistlethorn Acorn, Amanita Charm, Genji''s Guard, Shield of the Phoenix,
    Kinetic Cuirass, Berserker''s Shield, The Crusher, Eye of Providence, Shifter''s
    Shield, The Reaper, Runeforged Hammer, Oni Hunter''s Garb, Eye of the Storm, Shield
    Splitter, Chandra''s Grace, Hydra''s Lament, Erosion, Phoenix Feather, Spectral
    Armor, Riptalon, Freya''s Tears, Avenging Blade, Draconic Scale, Breastplate of
    Valor, Golden Blade, Pharaoh''s Curse, Yogi''s Necklace, Leviathan''s Hide.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.64
      efficiency: 0.98
      win: 0.48
      pick: 0.27
      fit: 0.44
    Thistlethorn Acorn:
      total: 0.68
      efficiency: 0.95
      win: 0.6
      pick: 0.15
      fit: 0.48
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.65
      pick: 0.1
      fit: 0.21
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Genji's Guard
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Thistlethorn Acorn, The Crusher, Genji''s Guard, The Reaper, Titan''s
    Bane, Tekko-Kagi, Pendulum Blade, Avatar''s Parashu, Avenging Blade, Riptalon,
    Hydra''s Lament, Silverbranch Bow, Heartseeker, Runeforged Hammer, Lernaean Bow,
    Damaru, Berserker''s Shield, Golden Blade, Toxic Blade, Screeching Gargoyle, Breastplate
    of Valor, Shield Splitter, Dominance, Oath-Sworn Spear, Arondight, Eye of the
    Storm, Amanita Charm, Tyrfing.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.98
      win: 0.48
      pick: 0.27
      fit: 0.33
    Thistlethorn Acorn:
      total: 0.67
      efficiency: 0.95
      win: 0.6
      pick: 0.15
      fit: 0.38
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.65
      pick: 0.1
      fit: 0.06
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.45
      pick: 0.21
      fit: 1.0
    The Crusher:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.54
      efficiency: 0.46
      win: 0.52
      pick: 0.12
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Berserker's Shield
  - Riptalon
  flex_slots:
  - Golden Blade
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Thistlethorn Acorn, Genji''s Guard, Riptalon, Golden Blade, Berserker''s
    Shield, Silverbranch Bow, The Crusher, Tyrfing, Lernaean Bow, Dominance, Tekko-Kagi,
    Hydra''s Lament, The Reaper, Toxic Blade, Runeforged Hammer, Pharaoh''s Curse,
    Breastplate of Valor, Damaru, Shogun''s Ofuda, Amanita Charm, Oni Hunter''s Garb,
    Yogi''s Necklace, Eros'' Bow, Kinetic Cuirass, Qin''s Blade, Avenging Blade, Eye
    of Providence, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.69
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.98
      win: 0.48
      pick: 0.27
      fit: 0.48
    Thistlethorn Acorn:
      total: 0.65
      efficiency: 0.95
      win: 0.6
      pick: 0.15
      fit: 0.31
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.65
      pick: 0.1
      fit: 0.04
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.31
    Riptalon:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  flex_slots:
  - Hydra's Lament
  - Breastplate of Valor
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Thistlethorn Acorn, Genji''s Guard,
    Hydra''s Lament, Breastplate of Valor, The Crusher, Shield of the Phoenix, Freya''s
    Tears, Pendulum Blade, Arondight, Screeching Gargoyle, Chandra''s Grace, Berserker''s
    Shield, Runeforged Hammer, The Reaper, Gladiator''s Shield, Lernaean Bow, Amanita
    Charm, Damaru, Oni Hunter''s Garb, Yogi''s Necklace, Kinetic Cuirass, Riptalon,
    Prophetic Cloak, Silverbranch Bow, Avenging Blade, Regrowth Striders, Eye of Providence,
    Heartseeker.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.6
      efficiency: 0.98
      win: 0.48
      pick: 0.27
      fit: 0.15
    Thistlethorn Acorn:
      total: 0.71
      efficiency: 0.95
      win: 0.6
      pick: 0.15
      fit: 0.65
    Genji's Guard:
      total: 0.62
      efficiency: 0.72
      win: 0.65
      pick: 0.1
      fit: 0.5
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.45
      pick: 0.21
      fit: 0.85
    Hydra's Lament:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Ashwhorl Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Thistlethorn Acorn, The Crusher, The Reaper, Hydra''s
    Lament, Heartseeker, Runeforged Hammer, Titan''s Bane, Pendulum Blade, Tekko-Kagi,
    Lernaean Bow, Avatar''s Parashu, Damaru, Avenging Blade, Golden Blade, Arondight,
    Shield Splitter, Genji''s Guard, Dominance, Eye of the Storm, Tyrfing, Riptalon,
    Silverbranch Bow, Berserker''s Shield, Barbed Carver, Breastplate of Valor, Transcendence,
    Bloodforge, Musashi''s Dual Swords.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.98
      win: 0.48
      pick: 0.27
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.7
      efficiency: 0.95
      win: 0.6
      pick: 0.15
      fit: 0.61
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.45
      pick: 0.21
      fit: 1.0
    Hydra's Lament:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.71
    The Crusher:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.51
      efficiency: 0.46
      win: 0.42
      pick: 0.11
      fit: 1.0
  starter: *id001
---
