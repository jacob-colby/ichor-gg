---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.5
  aspect_win_rate: 0.6
  slot_order:
  - name: Transcendence
    pick_rate: 0.15
    win_rate: 0.33
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.33
    - name: Eye of the Storm
      pick_rate: 0.1
      win_rate: 0.5
  - name: Shifter's Shield
    pick_rate: 0.15
    win_rate: 0.33
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 1.0
    - name: Contagion
      pick_rate: 0.05
      win_rate: 0.0
  - name: Breastplate of Valor
    pick_rate: 0.17
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Mystical Mail
      pick_rate: 0.11
      win_rate: 0.0
  - name: Totem of Death
    pick_rate: 0.19
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.0
    - name: Contagion
      pick_rate: 0.06
      win_rate: 0.0
  - name: Mote of Chaos
    pick_rate: 0.13
    win_rate: 0.0
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.5
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 1.0
  - name: Engraved Guard
    pick_rate: 0.25
    win_rate: 0.5
    alternates:
    - name: Mana Tome
      pick_rate: 0.13
      win_rate: 1.0
    - name: Helm of Radiance
      pick_rate: 0.13
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.35
    win_rate: 0.71
  - name: Bluestone Pendant
    pick_rate: 0.35
    win_rate: 0.29
  - name: Conduit Gem
    pick_rate: 0.1
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-08-14'
  god_win_rate: 0.45
  god_matches_won: 9
  god_matches_played: 20
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Eye of the Storm
  - Helm of Radiance
  - Gluttonous Grimoire
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Eye of the Storm
  - Gluttonous Grimoire
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
    this god: Jotunn''s Revenge, Eye of the Storm, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, The Crusher, Berserker''s Shield, Soul Gem, Freya''s Tears, Nimble
    Ring, Oni Hunter''s Garb, Shield of the Phoenix, Shield Splitter, Runeforged Hammer,
    The Cosmic Horror, Erosion, Hydra''s Lament, Spectral Armor, Eye of Providence,
    Spear of the Magus, Death Metal, Draconic Scale, Spear of Desolation, Pharaoh''s
    Curse, Leviathan''s Hide, Rod of Asclepius, Midgardian Mail, Golden Blade, The
    Reaper, Mantle Of Discord, Stone of Binding, Jade Scepter, Obsidian Shard, Avenging
    Blade, Chronos'' Pendant, Damaru.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.64
      win: 1.0
      pick: 0.14
      fit: 0.4
    Eye of the Storm:
      total: 0.47
      efficiency: 0.5
      win: 0.5
      pick: 0.1
      fit: 0.46
    Helm of Radiance:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.4
      fit: 0.31
    Gluttonous Grimoire:
      total: 0.45
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.53
    Heartseeker:
      total: 0.66
      efficiency: 0.41
      win: 1.0
      pick: 0.13
      fit: 0.42
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.77
      win: 0.5
      pick: 0.28
      fit: 0.3
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Eye of the Storm
  - Helm of Radiance
  - Gluttonous Grimoire
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Eye of the Storm
  - Gluttonous Grimoire
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Eye of the Storm, Gluttonous Grimoire, The Crusher, Kinetic Cuirass,
    Amanita Charm, Soul Gem, Nimble Ring, Berserker''s Shield, Hydra''s Lament, Oni
    Hunter''s Garb, Freya''s Tears, Death Metal, Runeforged Hammer, The Cosmic Horror,
    Shield of the Phoenix, Shield Splitter, Spear of the Magus, Spear of Desolation,
    Spectral Armor, Erosion, Rod of Asclepius, Eye of Providence, Chronos'' Pendant,
    Draconic Scale, Golden Blade, Jade Scepter, The Reaper, Pharaoh''s Curse, Obsidian
    Shard, Damaru, Leviathan''s Hide, Avenging Blade, Yogi''s Necklace, Midgardian
    Mail, Bancroft''s Talon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.64
      win: 1.0
      pick: 0.14
      fit: 0.45
    Eye of the Storm:
      total: 0.47
      efficiency: 0.5
      win: 0.5
      pick: 0.1
      fit: 0.42
    Helm of Radiance:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.4
      fit: 0.31
    Gluttonous Grimoire:
      total: 0.44
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.5
    Heartseeker:
      total: 0.67
      efficiency: 0.41
      win: 1.0
      pick: 0.13
      fit: 0.46
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.5
      pick: 0.28
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Eye of the Storm
  - Helm of Radiance
  - Gluttonous Grimoire
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Eye of the Storm
  - Gluttonous Grimoire
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Eye of the Storm, Gluttonous Grimoire, The Crusher, Soul
    Gem, Kinetic Cuirass, Amanita Charm, Freya''s Tears, Berserker''s Shield, Nimble
    Ring, Shield of the Phoenix, The Cosmic Horror, Spear of Desolation, Spear of
    the Magus, Oni Hunter''s Garb, Hydra''s Lament, Runeforged Hammer, Shield Splitter,
    Spectral Armor, Erosion, Death Metal, Eye of Providence, The Reaper, Obsidian
    Shard, Chronos'' Pendant, Draconic Scale, Pharaoh''s Curse, Rod of Asclepius,
    Screeching Gargoyle, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Golden
    Blade, Chandra''s Grace, Jade Scepter, Stone of Binding.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.64
      win: 1.0
      pick: 0.14
      fit: 0.48
    Eye of the Storm:
      total: 0.46
      efficiency: 0.5
      win: 0.5
      pick: 0.1
      fit: 0.38
    Helm of Radiance:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.4
      fit: 0.27
    Gluttonous Grimoire:
      total: 0.45
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.67
      efficiency: 0.41
      win: 1.0
      pick: 0.13
      fit: 0.44
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.5
      pick: 0.28
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Eye of the Storm
  - Helm of Radiance
  - Heartseeker
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Eye of the Storm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Eye of the Storm, Soul Gem, Gluttonous
    Grimoire, Shield of the Phoenix, The Crusher, Kinetic Cuirass, Rod of Asclepius,
    The Reaper, Berserker''s Shield, Chandra''s Grace, Nimble Ring, Blood-Bound Book,
    Oni Hunter''s Garb, Runeforged Hammer, Freya''s Tears, Riptalon, Bancroft''s Talon,
    Lifebinder, The Cosmic Horror, Phoenix Feather, Hydra''s Lament, Spectral Armor,
    Spear of the Magus, Death Metal, Erosion, Shield Splitter, Spear of Desolation,
    Eye of Providence, Draconic Scale, Golden Blade, Pharaoh''s Curse, Leviathan''s
    Hide, Avenging Blade, Jade Scepter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.64
      win: 1.0
      pick: 0.14
      fit: 0.42
    Eye of the Storm:
      total: 0.48
      efficiency: 0.5
      win: 0.5
      pick: 0.1
      fit: 0.47
    Helm of Radiance:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.4
      fit: 0.29
    Heartseeker:
      total: 0.67
      efficiency: 0.41
      win: 1.0
      pick: 0.13
      fit: 0.43
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.77
      win: 0.5
      pick: 0.28
      fit: 0.31
    Amanita Charm:
      total: 0.48
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Eye of the Storm
  - Helm of Radiance
  - Gluttonous Grimoire
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Eye of the Storm
  - Gluttonous Grimoire
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Eye of the Storm, Gluttonous Grimoire, The Crusher,
    Soul Gem, Kinetic Cuirass, Amanita Charm, Stone of Binding, Berserker''s Shield,
    Avenging Blade, The Cosmic Horror, Screeching Gargoyle, Spear of the Magus, Nimble
    Ring, Void Shield, Freya''s Tears, Spear of Desolation, Oni Hunter''s Garb, Void
    Stone, Shield of the Phoenix, Runeforged Hammer, The Reaper, Hydra''s Lament,
    Obsidian Shard, Shield Splitter, Spectral Armor, Erosion, Death Metal, Eye of
    Providence, Draconic Scale, Pharaoh''s Curse, Riptalon, Rod of Asclepius, Leviathan''s
    Hide, Midgardian Mail, Golden Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.64
      win: 1.0
      pick: 0.14
      fit: 0.49
    Eye of the Storm:
      total: 0.46
      efficiency: 0.5
      win: 0.5
      pick: 0.1
      fit: 0.39
    Helm of Radiance:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.4
      fit: 0.27
    Gluttonous Grimoire:
      total: 0.46
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.61
    Heartseeker:
      total: 0.68
      efficiency: 0.41
      win: 1.0
      pick: 0.13
      fit: 0.52
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.5
      pick: 0.28
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Helm of Radiance
  - Nimble Ring
  - Heartseeker
  flex_slots:
  - Berserker's Shield
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Eye of the Storm, Gluttonous Grimoire, Nimble Ring,
    Berserker''s Shield, Kinetic Cuirass, The Crusher, Amanita Charm, Soul Gem, Golden
    Blade, Riptalon, Freya''s Tears, Pharaoh''s Curse, Oni Hunter''s Garb, Silverbranch
    Bow, Shield of the Phoenix, The Cosmic Horror, Runeforged Hammer, Spectral Armor,
    Hydra''s Lament, Shogun''s Ofuda, Spear of the Magus, Tyrfing, Lernaean Bow, Erosion,
    Shield Splitter, Death Metal, Eye of Providence, Spear of Desolation, Toxic Blade,
    Draconic Scale, Rod of Asclepius, Leviathan''s Hide, The Reaper, Bracer of The
    Abyss, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.4
      efficiency: 0.53
      win: 0.33
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.43
      efficiency: 0.66
      win: 0.33
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.64
      win: 1.0
      pick: 0.14
      fit: 0.25
    Helm of Radiance:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.4
      fit: 0.22
    Nimble Ring:
      total: 0.44
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.33
    Heartseeker:
      total: 0.64
      efficiency: 0.41
      win: 1.0
      pick: 0.13
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Helm of Radiance
  - Freya's Tears
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Eye of the Storm,
    Freya''s Tears, Soul Gem, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Shield of the Phoenix, The Crusher, Berserker''s Shield, Hydra''s Lament, Spear
    of Desolation, Oni Hunter''s Garb, Nimble Ring, Screeching Gargoyle, Chronos''
    Pendant, Chandra''s Grace, Erosion, Gladiator''s Shield, Spectral Armor, Eye of
    Providence, Runeforged Hammer, The Cosmic Horror, Prophetic Cloak, Shield Splitter,
    Draconic Scale, Spear of the Magus, Pharaoh''s Curse, Leviathan''s Hide, Midgardian
    Mail, Gem of Focus, Mantle Of Discord, Stone of Binding, Death Metal, Arondight.'
  slot_scores:
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.64
      win: 0.33
      pick: 0.26
      fit: 0.43
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.64
      win: 1.0
      pick: 0.14
      fit: 0.51
    Helm of Radiance:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.4
      fit: 0.23
    Freya's Tears:
      total: 0.44
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.58
    Heartseeker:
      total: 0.65
      efficiency: 0.41
      win: 1.0
      pick: 0.13
      fit: 0.32
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.5
      pick: 0.28
      fit: 0.22
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    The Crusher, Jotunn''s Revenge, Berserker''s Shield, Soul Gem, Freya''s Tears,
    Nimble Ring, Oni Hunter''s Garb, Shield of the Phoenix, Shield Splitter, Runeforged
    Hammer, The Cosmic Horror, Erosion, Hydra''s Lament, Spectral Armor, Eye of Providence,
    Spear of the Magus, Eye of the Storm, Death Metal, Draconic Scale, Spear of Desolation,
    Pharaoh''s Curse, Leviathan''s Hide, Rod of Asclepius, Midgardian Mail, Golden
    Blade, The Reaper, Mantle Of Discord, Stone of Binding, Jade Scepter, Obsidian
    Shard, Avenging Blade, Chronos'' Pendant, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.29
      efficiency: 0.69
      win: 0.0
      pick: 0.22
      fit: 0.24
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.64
      win: 1.0
      pick: 0.14
      fit: 0.4
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.59
      win: 0.33
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.45
      efficiency: 0.63
      win: 0.33
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.44
      efficiency: 0.64
      win: 0.33
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.77
      win: 0.5
      pick: 0.28
      fit: 0.3
  starter: *id001
---
