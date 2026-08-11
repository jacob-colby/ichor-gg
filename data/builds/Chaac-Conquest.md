---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.42
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.4
    win_rate: 0.48
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.11
      win_rate: 0.54
    - name: Transcendence
      pick_rate: 0.07
      win_rate: 0.63
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.41
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.61
    - name: Shield of the Phoenix
      pick_rate: 0.07
      win_rate: 0.67
  - name: Gladiator's Shield
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.38
  - name: Shield of the Phoenix
    pick_rate: 0.06
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.71
  - name: Dwarven Plate
    pick_rate: 0.05
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.86
    - name: Kinetic Cuirass
      pick_rate: 0.05
      win_rate: 0.2
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.5
    - name: Captain's Ring
      pick_rate: 0.04
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.36
    win_rate: 0.6
  - name: Bluestone Pendant
    pick_rate: 0.33
    win_rate: 0.45
  - name: Sundering Axe
    pick_rate: 0.12
    win_rate: 0.73
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-08-10'
  god_win_rate: 0.512396694214876
  god_matches_won: 62
  god_matches_played: 121
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Gluttonous Grimoire, Jotunn''s Revenge, Shield of the
    Phoenix, Amanita Charm, The Crusher, Berserker''s Shield, Soul Gem, Breastplate
    of Valor, Oni Hunter''s Garb, Hydra''s Lament, Spear of the Magus, Shield Splitter,
    Death Metal, Runeforged Hammer, Helm of Radiance, The Cosmic Horror, Erosion,
    Spectral Armor, Eye of the Storm, Eye of Providence, Pharaoh''s Curse, Spear of
    Desolation, Draconic Scale, Rod of Asclepius, Jade Scepter, Obsidian Shard, Leviathan''s
    Hide, Golden Blade, Midgardian Mail, Mantle Of Discord, Stone of Binding, Chronos''
    Pendant, Damaru, Lernaean Bow, The Reaper, Avenging Blade, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.29
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.71
      pick: 0.1
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: burst
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Freya''s Tears, Gluttonous Grimoire, Jotunn''s Revenge, Soul Gem, Shield
    of the Phoenix, The Crusher, Amanita Charm, Berserker''s Shield, Breastplate of
    Valor, Spear of the Magus, Hydra''s Lament, Oni Hunter''s Garb, Spear of Desolation,
    The Cosmic Horror, Death Metal, Runeforged Hammer, Helm of Radiance, Shield Splitter,
    Obsidian Shard, Spectral Armor, Erosion, Pharaoh''s Curse, Chronos'' Pendant,
    Eye of Providence, Rod of Asclepius, Eye of the Storm, The Reaper, Draconic Scale,
    Jade Scepter, Leviathan''s Hide, Screeching Gargoyle, Riptalon, Golden Blade,
    Midgardian Mail, Damaru, Mantle Of Discord, Lernaean Bow, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.71
      pick: 0.1
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Shield of the Phoenix, Amanita Charm, Soul Gem, Gluttonous
    Grimoire, Jotunn''s Revenge, Rod of Asclepius, The Crusher, Berserker''s Shield,
    The Reaper, Blood-Bound Book, Bancroft''s Talon, Chandra''s Grace, Breastplate
    of Valor, Riptalon, Oni Hunter''s Garb, Runeforged Hammer, Hydra''s Lament, Spear
    of the Magus, Lifebinder, Death Metal, The Cosmic Horror, Phoenix Feather, Spectral
    Armor, Eye of the Storm, Shield Splitter, Helm of Radiance, Erosion, Pharaoh''s
    Curse, Spear of Desolation, Jade Scepter, Eye of Providence, Golden Blade, Draconic
    Scale, Obsidian Shard, Leviathan''s Hide, Avenging Blade, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.57
      pick: 0.1
      fit: 0.68
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.71
      pick: 0.1
      fit: 0.35
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher,
    Soul Gem, Shield of the Phoenix, Amanita Charm, Berserker''s Shield, Spear of
    the Magus, Stone of Binding, Avenging Blade, The Cosmic Horror, Screeching Gargoyle,
    Breastplate of Valor, Void Shield, Oni Hunter''s Garb, Spear of Desolation, Hydra''s
    Lament, Obsidian Shard, Void Stone, Runeforged Hammer, Death Metal, The Reaper,
    Shield Splitter, Helm of Radiance, Spectral Armor, Erosion, Pharaoh''s Curse,
    Riptalon, Eye of Providence, Eye of the Storm, Heartseeker, Rod of Asclepius,
    Draconic Scale, Doom Orb, The World Stone, Jade Scepter, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.71
      pick: 0.1
      fit: 0.34
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.4
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - Riptalon
  flex_slots:
  - Riptalon
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Gluttonous Grimoire, Berserker''s Shield, Shield of
    the Phoenix, Soul Gem, Jotunn''s Revenge, Amanita Charm, The Crusher, Riptalon,
    Golden Blade, Breastplate of Valor, Pharaoh''s Curse, Oni Hunter''s Garb, Silverbranch
    Bow, Lernaean Bow, Spear of the Magus, Hydra''s Lament, Shogun''s Ofuda, Bracer
    of The Abyss, The Cosmic Horror, Helm of Radiance, Runeforged Hammer, Death Metal,
    Spectral Armor, Tyrfing, Erosion, Shield Splitter, Blood-Bound Book, Rod of Asclepius,
    Bancroft''s Talon, Eye of Providence, Jade Scepter, Spear of Desolation, Bragi''s
    Harp, Leviathan''s Hide, Obsidian Shard, Draconic Scale, Kinetic Cuirass.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.25
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.71
      pick: 0.1
      fit: 0.28
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Riptalon:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Shield of the Phoenix,
    Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire, Breastplate of Valor, Amanita
    Charm, Berserker''s Shield, Hydra''s Lament, The Crusher, Spear of Desolation,
    Oni Hunter''s Garb, Chronos'' Pendant, Screeching Gargoyle, Gladiator''s Shield,
    Spear of the Magus, Chandra''s Grace, Spectral Armor, Erosion, Eye of Providence,
    Pharaoh''s Curse, Runeforged Hammer, Shield Splitter, Helm of Radiance, The Cosmic
    Horror, Prophetic Cloak, Draconic Scale, Gem of Focus, Death Metal, Leviathan''s
    Hide, Eye of the Storm, Rod of Asclepius, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Jade Scepter, Yogi''s Necklace, Kinetic Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.41
      pick: 0.19
      fit: 0.43
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.26
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.51
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.1
      fit: 0.55
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.71
      pick: 0.1
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge, Kinetic Cuirass,
    Amanita Charm, The Crusher, Berserker''s Shield, Soul Gem, Breastplate of Valor,
    Freya''s Tears, Oni Hunter''s Garb, Hydra''s Lament, Spear of the Magus, Shield
    Splitter, Shield of the Phoenix, Death Metal, Runeforged Hammer, Helm of Radiance,
    The Cosmic Horror, Erosion, Spectral Armor, Eye of the Storm, Eye of Providence,
    Pharaoh''s Curse, Spear of Desolation, Draconic Scale, Rod of Asclepius, Jade
    Scepter, Obsidian Shard, Leviathan''s Hide, Golden Blade, Midgardian Mail, Mantle
    Of Discord, Stone of Binding, Chronos'' Pendant, Damaru, Lernaean Bow, The Reaper,
    Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.71
      win: 0.41
      pick: 0.19
      fit: 0.24
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.38
      efficiency: 0.59
      win: 0.2
      pick: 0.11
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
---
