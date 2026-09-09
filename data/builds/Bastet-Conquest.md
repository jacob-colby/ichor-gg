---
type: smite-build
god: Bastet
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Watchful Pride
  aspect_pick_rate: 0.1
  aspect_win_rate: 1.0
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.75
    win_rate: 0.5
    alternates:
    - name: Barbed Carver
      pick_rate: 0.13
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.04
      win_rate: 1.0
  - name: Barbed Carver
    pick_rate: 0.31
    win_rate: 0.6
    alternates:
    - name: Transcendence
      pick_rate: 0.23
      win_rate: 0.45
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.2
  - name: The Crusher
    pick_rate: 0.23
    win_rate: 0.45
    alternates:
    - name: Barbed Carver
      pick_rate: 0.21
      win_rate: 0.5
    - name: Pendulum Blade
      pick_rate: 0.13
      win_rate: 0.33
  - name: Heartseeker
    pick_rate: 0.3
    win_rate: 0.5
    alternates:
    - name: The Crusher
      pick_rate: 0.15
      win_rate: 0.71
    - name: Titan's Bane
      pick_rate: 0.15
      win_rate: 0.57
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.71
    alternates:
    - name: Heartseeker
      pick_rate: 0.3
      win_rate: 0.77
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.0
  - name: Blinking Abyss
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Skeggox
      pick_rate: 0.1
      win_rate: 0.33
    - name: Titan's Bane
      pick_rate: 0.1
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.29
    win_rate: 0.64
  - name: Bluestone Pendant
    pick_rate: 0.21
    win_rate: 0.4
  - name: Pendulum of the Ages
    pick_rate: 0.13
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/bastet/
  last_verified: '2026-09-09'
  god_win_rate: 0.5833333333333334
  god_matches_won: 28
  god_matches_played: 48
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Avatar''s Parashu, Tekko-Kagi, Tyrfing, Arondight, Runeforged
    Hammer, Avenging Blade, Golden Blade, Silverbranch Bow, Lernaean Bow, Shield Splitter,
    Dominance, Riptalon, Oath-Sworn Spear, Toxic Blade, Bloodforge, Deathbringer,
    Eye of the Storm, Damaru, Rage, Musashi''s Dual Swords, Sanguine Lash, Hydra''s
    Lament.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.5
      pick: 0.75
      fit: 1.0
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.45
      pick: 0.31
      fit: 0.52
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.91
    Shifter's Shield:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.04
      fit: 0.0
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.5
      fit: 1.0
    Titan's Bane:
      total: 0.65
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Crusher
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Reaper, Arondight, Avatar''s Parashu, Tyrfing, Runeforged Hammer, Tekko-Kagi,
    Avenging Blade, Dominance, Breastplate of Valor, Lernaean Bow, Genji''s Guard,
    Shield Splitter, Golden Blade, Oath-Sworn Spear, Silverbranch Bow, Daybreak Gavel,
    Riptalon, Bloodforge, Yogi''s Necklace, Toxic Blade, Deathbringer, Eye of the
    Storm, Hydra''s Lament.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.5
      pick: 0.75
      fit: 0.71
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.45
      pick: 0.31
      fit: 0.39
    Shifter's Shield:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.04
      fit: 0.0
    The Crusher:
      total: 0.47
      efficiency: 0.47
      win: 0.45
      pick: 0.36
      fit: 0.57
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.5
      pick: 0.5
      fit: 0.77
    Titan's Bane:
      total: 0.59
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Crusher
  - Transcendence
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
    god: The Reaper, Arondight, Avatar''s Parashu, Tekko-Kagi, Tyrfing, Runeforged
    Hammer, Silverbranch Bow, Avenging Blade, Breastplate of Valor, Riptalon, Genji''s
    Guard, Toxic Blade, Lernaean Bow, Shield Splitter, Dominance, Golden Blade, Daybreak
    Gavel, Oath-Sworn Spear, Eye of Erebus, Screeching Gargoyle, Bloodforge, Chandra''s
    Grace, Hydra''s Lament.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.5
      pick: 0.75
      fit: 0.78
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.45
      pick: 0.31
      fit: 0.22
    Shifter's Shield:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.04
      fit: 0.0
    The Crusher:
      total: 0.48
      efficiency: 0.47
      win: 0.45
      pick: 0.36
      fit: 0.66
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.5
      pick: 0.5
      fit: 0.76
    Titan's Bane:
      total: 0.6
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 0.66
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix,
    Runeforged Hammer, The Reaper, Shield Splitter, Eye of the Storm, Freya''s Tears,
    Berserker''s Shield, Erosion, Eye of Providence, Genji''s Guard, Breastplate of
    Valor, Draconic Scale, Yogi''s Necklace, Phoenix Feather, Avenging Blade, Stone
    of Binding, Midgardian Mail, Chandra''s Grace, Daybreak Gavel, Hide of the Nemean
    Lion, Magi''s Cloak, Leviathan''s Hide, Hydra''s Lament.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.75
      fit: 0.44
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.73
    Shifter's Shield:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.04
      fit: 0.56
    Titan's Bane:
      total: 0.58
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Shifter's Shield
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Avatar''s Parashu, Tekko-Kagi, Avenging Blade, Silverbranch
    Bow, Riptalon, Tyrfing, Toxic Blade, Oath-Sworn Spear, Arondight, Runeforged Hammer,
    Golden Blade, Lernaean Bow, Shield Splitter, Dominance, Screeching Gargoyle, Daybreak
    Gavel, Bloodforge, Breastplate of Valor, Genji''s Guard, Deathbringer, Eye of
    the Storm, Hydra''s Lament.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.5
      pick: 0.75
      fit: 1.0
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.94
    Shifter's Shield:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.04
      fit: 0.0
    The Crusher:
      total: 0.53
      efficiency: 0.47
      win: 0.45
      pick: 0.36
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.5
      fit: 1.0
    Titan's Bane:
      total: 0.65
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Shifter's Shield
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
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
    Blade, The Reaper, Toxic Blade, Dominance, Qin''s Blade, Sun Beam Bow, Berserker''s
    Shield, Avatar''s Parashu, Dagger of Frenzy, Arondight, Runeforged Hammer, Avenging
    Blade, Vital Amplifier, Hastened Fatalis, Bloodforge, The Executioner, Odysseus''
    Bow, Hydra''s Lament.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.75
      fit: 0.37
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Shifter's Shield:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.04
      fit: 0.0
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
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 0.43
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Arondight
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Arondight, Breastplate of Valor, Genji''s
    Guard, The Reaper, Avatar''s Parashu, Tyrfing, Eye of Erebus, Screeching Gargoyle,
    Runeforged Hammer, Chandra''s Grace, Freya''s Tears, Tekko-Kagi, Avenging Blade,
    Shield of the Phoenix, Silverbranch Bow, Daybreak Gavel, Riptalon, Lernaean Bow,
    Hydra''s Lament, Golden Blade, Gladiator''s Shield, Shield Splitter, Dominance,
    Toxic Blade.'
  slot_scores:
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.5
      pick: 0.75
      fit: 0.85
    Arondight:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shifter's Shield:
      total: 0.55
      efficiency: 0.28
      win: 1.0
      pick: 0.04
      fit: 0.0
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.5
      fit: 0.55
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Reaper, Hydra''s Lament, Avatar''s Parashu, Tekko-Kagi,
    Tyrfing, Arondight, Runeforged Hammer, Avenging Blade, Golden Blade, Silverbranch
    Bow, Lernaean Bow, Shield Splitter, Dominance, Riptalon, Oath-Sworn Spear, Toxic
    Blade, Bloodforge, Deathbringer, Eye of the Storm, Damaru, Rage, Musashi''s Dual
    Swords, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.5
      pick: 0.75
      fit: 1.0
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.91
    Pendulum Blade:
      total: 0.46
      efficiency: 0.42
      win: 0.33
      pick: 0.2
      fit: 1.0
    The Crusher:
      total: 0.53
      efficiency: 0.47
      win: 0.45
      pick: 0.36
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.5
      fit: 1.0
    Titan's Bane:
      total: 0.65
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
---
