---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.71
  slot_order:
  - name: Briskberry Acorn
    pick_rate: 0.44
    win_rate: 0.53
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.29
      win_rate: 0.4
    - name: Ashwhorl Acorn
      pick_rate: 0.12
      win_rate: 0.5
  - name: Ashwhorl Acorn
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.41
      win_rate: 0.43
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.33
  - name: Thistlethorn Acorn
    pick_rate: 0.32
    win_rate: 0.36
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.5
    - name: Briskberry Acorn
      pick_rate: 0.09
      win_rate: 0.67
  - name: Heartseeker
    pick_rate: 0.15
    win_rate: 0.4
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.33
    - name: Transcendence
      pick_rate: 0.09
      win_rate: 0.33
  - name: Titan's Bane
    pick_rate: 0.27
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.23
      win_rate: 0.29
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.33
  - name: Lucerne Hammer
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.33
    - name: Blinking Abyss
      pick_rate: 0.12
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.35
    win_rate: 0.42
  - name: Bluestone Brooch
    pick_rate: 0.24
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-08-27'
  god_win_rate: 0.5
  god_matches_won: 17
  god_matches_played: 34
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Pendulum Blade
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Pendulum Blade, Hydra''s Lament, Avatar''s Parashu, Tekko-Kagi,
    Tyrfing, Arondight, Runeforged Hammer, Avenging Blade, Golden Blade, Lernaean
    Bow, Shield Splitter, Dominance, Silverbranch Bow, Oath-Sworn Spear, Barbed Carver,
    Riptalon, Bloodforge, Toxic Blade, Deathbringer, Eye of the Storm, Damaru, Rage.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.16
      fit: 0.52
    Briskberry Acorn:
      total: 0.59
      efficiency: 0.71
      win: 0.53
      pick: 0.44
      fit: 0.52
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.5
      pick: 0.19
      fit: 1.0
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.91
    Pendulum Blade:
      total: 0.52
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.58
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Heartseeker
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, The Reaper, Arondight, Pendulum Blade, Avatar''s Parashu, Runeforged Hammer,
    Tyrfing, Tekko-Kagi, Avenging Blade, Dominance, Breastplate of Valor, Lernaean
    Bow, Genji''s Guard, Shield Splitter, Golden Blade, Oath-Sworn Spear, Daybreak
    Gavel, Silverbranch Bow, Barbed Carver, Bloodforge, Riptalon, Yogi''s Necklace,
    Deathbringer.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.16
      fit: 0.29
    Briskberry Acorn:
      total: 0.55
      efficiency: 0.71
      win: 0.53
      pick: 0.44
      fit: 0.29
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.5
      pick: 0.19
      fit: 0.71
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.63
    Heartseeker:
      total: 0.47
      efficiency: 0.47
      win: 0.4
      pick: 0.25
      fit: 0.77
    Titan's Bane:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.58
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Hydra's Lament
  - Titan's Bane
  flex_slots:
  - Thistlethorn Acorn
  - Hydra's Lament
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Hydra''s Lament, Pendulum Blade, The Reaper, Arondight, Avatar''s Parashu,
    Tekko-Kagi, Runeforged Hammer, Tyrfing, Avenging Blade, Silverbranch Bow, Breastplate
    of Valor, Genji''s Guard, Riptalon, Lernaean Bow, Shield Splitter, Dominance,
    Toxic Blade, Daybreak Gavel, Golden Blade, Oath-Sworn Spear, Barbed Carver, Eye
    of Erebus, Screeching Gargoyle.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.16
      fit: 0.22
    Briskberry Acorn:
      total: 0.54
      efficiency: 0.71
      win: 0.53
      pick: 0.44
      fit: 0.22
    Thistlethorn Acorn:
      total: 0.5
      efficiency: 0.72
      win: 0.36
      pick: 0.5
      fit: 0.44
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.19
      fit: 0.78
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.54
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.58
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Thistlethorn Acorn
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Runeforged Hammer,
    The Reaper, Shield Splitter, Shifter''s Shield, Eye of the Storm, Freya''s Tears,
    Berserker''s Shield, Erosion, Eye of Providence, Genji''s Guard, Breastplate of
    Valor, Draconic Scale, Yogi''s Necklace, Phoenix Feather, Avenging Blade, Hydra''s
    Lament, Stone of Binding, Midgardian Mail, Chandra''s Grace, Daybreak Gavel, Hide
    of the Nemean Lion.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.58
      efficiency: 0.8
      win: 0.5
      pick: 0.16
      fit: 0.44
    Briskberry Acorn:
      total: 0.61
      efficiency: 0.82
      win: 0.53
      pick: 0.44
      fit: 0.44
    Thistlethorn Acorn:
      total: 0.55
      efficiency: 0.82
      win: 0.36
      pick: 0.5
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.19
      fit: 0.44
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Jotunn's Revenge
  - The Reaper
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Ashwhorl Acorn
  - Avatar's Parashu
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Avatar''s Parashu, Pendulum Blade, Tekko-Kagi, Avenging
    Blade, Hydra''s Lament, Silverbranch Bow, Riptalon, Oath-Sworn Spear, Arondight,
    Tyrfing, Runeforged Hammer, Toxic Blade, Lernaean Bow, Shield Splitter, Dominance,
    Golden Blade, Barbed Carver, Screeching Gargoyle, Daybreak Gavel, Bloodforge,
    Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.16
      fit: 0.33
    Briskberry Acorn:
      total: 0.56
      efficiency: 0.71
      win: 0.53
      pick: 0.44
      fit: 0.33
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.5
      pick: 0.19
      fit: 1.0
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.94
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.58
      fit: 1.0
    Avatar's Parashu:
      total: 0.52
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Tyrfing, Silverbranch Bow, Tekko-Kagi, Lernaean Bow, Golden
    Blade, The Reaper, Toxic Blade, Dominance, Qin''s Blade, Hydra''s Lament, Sun
    Beam Bow, Berserker''s Shield, Avatar''s Parashu, Dagger of Frenzy, Arondight,
    Runeforged Hammer, Pendulum Blade, Avenging Blade, Barbed Carver, Vital Amplifier,
    Hastened Fatalis, Bloodforge.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.57
      efficiency: 0.76
      win: 0.5
      pick: 0.16
      fit: 0.48
    Briskberry Acorn:
      total: 0.54
      efficiency: 0.71
      win: 0.53
      pick: 0.44
      fit: 0.17
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.19
      fit: 0.37
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Hydra's Lament
  - Pendulum Blade
  flex_slots:
  - Ashwhorl Acorn
  - Pendulum Blade
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Pendulum Blade, Arondight,
    Breastplate of Valor, Genji''s Guard, The Reaper, Avatar''s Parashu, Eye of Erebus,
    Screeching Gargoyle, Runeforged Hammer, Tyrfing, Chandra''s Grace, Freya''s Tears,
    Tekko-Kagi, Avenging Blade, Shield of the Phoenix, Silverbranch Bow, Daybreak
    Gavel, Lernaean Bow, Gladiator''s Shield, Shield Splitter, Dominance, Riptalon.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.5
      efficiency: 0.7
      win: 0.5
      pick: 0.16
      fit: 0.15
    Briskberry Acorn:
      total: 0.53
      efficiency: 0.71
      win: 0.53
      pick: 0.44
      fit: 0.15
    Thistlethorn Acorn:
      total: 0.54
      efficiency: 0.72
      win: 0.36
      pick: 0.5
      fit: 0.65
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.5
      pick: 0.19
      fit: 0.85
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.75
    Pendulum Blade:
      total: 0.5
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - The Crusher
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Reaper, Pendulum Blade, Hydra''s Lament, Avatar''s
    Parashu, Tekko-Kagi, Tyrfing, Arondight, Runeforged Hammer, Avenging Blade, Golden
    Blade, Lernaean Bow, Shield Splitter, Dominance, Silverbranch Bow, Oath-Sworn
    Spear, Barbed Carver, Riptalon, Bloodforge, Toxic Blade, Deathbringer, Eye of
    the Storm, Damaru, Rage.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.16
      fit: 0.52
    Briskberry Acorn:
      total: 0.59
      efficiency: 0.71
      win: 0.53
      pick: 0.44
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.53
      efficiency: 0.72
      win: 0.36
      pick: 0.5
      fit: 0.61
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.5
      pick: 0.19
      fit: 1.0
    The Crusher:
      total: 0.47
      efficiency: 0.47
      win: 0.33
      pick: 0.22
      fit: 1.0
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.58
      fit: 1.0
  starter: *id001
---
