---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.44
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.53
    win_rate: 0.54
    alternates:
    - name: Mystical Mail
      pick_rate: 0.08
      win_rate: 0.75
    - name: Barbed Carver
      pick_rate: 0.06
      win_rate: 0.58
  - name: Shield of the Phoenix
    pick_rate: 0.28
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.2
      win_rate: 0.41
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.47
  - name: Gladiator's Shield
    pick_rate: 0.18
    win_rate: 0.74
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.15
      win_rate: 0.54
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.46
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 0.65
    - name: Shield of the Phoenix
      pick_rate: 0.07
      win_rate: 0.69
  - name: Kinetic Cuirass
    pick_rate: 0.09
    win_rate: 0.8
    alternates:
    - name: Draconic Scale
      pick_rate: 0.07
      win_rate: 0.73
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.8
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 0.7
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.14
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.71
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.49
    win_rate: 0.61
  - name: Bluestone Pendant
    pick_rate: 0.38
    win_rate: 0.43
  - name: Sands Of Time
    pick_rate: 0.05
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-08-14'
  god_win_rate: 0.5440414507772021
  god_matches_won: 105
  god_matches_played: 193
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Jotunn''s Revenge, Berserker''s
    Shield, The Crusher, Freya''s Tears, Breastplate of Valor, Oni Hunter''s Garb,
    Soul Gem, Shield Splitter, Hydra''s Lament, Erosion, Runeforged Hammer, Eye of
    Providence, Eye of the Storm, Spectral Armor, Pharaoh''s Curse, Leviathan''s Hide,
    Spear of the Magus, Golden Blade, Mantle Of Discord, Stone of Binding, Midgardian
    Mail, Death Metal, Helm of Radiance, The Cosmic Horror, Shogun''s Ofuda, Avenging
    Blade, Damaru, Lernaean Bow, The Reaper, Magi''s Cloak, Yogi''s Necklace, Screeching
    Gargoyle, Ancile, Rod of Asclepius.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.59
      win: 0.8
      pick: 0.19
      fit: 0.61
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.7
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.51
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Jotunn''s Revenge, Soul Gem, The Crusher, Amanita Charm,
    Berserker''s Shield, Breastplate of Valor, Freya''s Tears, Spear of the Magus,
    Hydra''s Lament, The Cosmic Horror, Oni Hunter''s Garb, Spear of Desolation, Runeforged
    Hammer, Helm of Radiance, Death Metal, Shield Splitter, Obsidian Shard, Spectral
    Armor, Erosion, Chronos'' Pendant, Pharaoh''s Curse, Eye of Providence, Rod of
    Asclepius, Eye of the Storm, The Reaper, Jade Scepter, Leviathan''s Hide, Screeching
    Gargoyle, Riptalon, Golden Blade, Midgardian Mail, Mantle Of Discord, Blood-Bound
    Book, Stone of Binding, Damaru.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.59
      win: 0.8
      pick: 0.19
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.63
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Jotunn''s Revenge, Berserker''s
    Shield, The Crusher, Rod of Asclepius, The Reaper, Chandra''s Grace, Oni Hunter''s
    Garb, Breastplate of Valor, Freya''s Tears, Runeforged Hammer, Riptalon, Hydra''s
    Lament, Eye of the Storm, Phoenix Feather, Blood-Bound Book, Shield Splitter,
    Erosion, Bancroft''s Talon, Spectral Armor, Eye of Providence, Pharaoh''s Curse,
    Golden Blade, Lifebinder, Leviathan''s Hide, Spear of the Magus, Avenging Blade,
    Midgardian Mail, Death Metal, Yogi''s Necklace, The Cosmic Horror, Shogun''s Ofuda,
    Glorious Pridwen, Damaru.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.59
      win: 0.8
      pick: 0.19
      fit: 0.6
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.66
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.7
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Stone of Binding
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Soul Gem, Amanita
    Charm, Berserker''s Shield, Stone of Binding, Avenging Blade, Screeching Gargoyle,
    Breastplate of Valor, Freya''s Tears, Void Shield, Spear of the Magus, Oni Hunter''s
    Garb, The Cosmic Horror, Hydra''s Lament, Void Stone, The Reaper, Runeforged Hammer,
    Shield Splitter, Spear of Desolation, Erosion, Spectral Armor, Riptalon, Eye of
    Providence, Obsidian Shard, Pharaoh''s Curse, Eye of the Storm, Heartseeker, Silverbranch
    Bow, Leviathan''s Hide, Death Metal, Helm of Radiance, Golden Blade, Midgardian
    Mail, Mantle Of Discord.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.48
      win: 0.7
      pick: 0.0
      fit: 0.7
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.59
      win: 0.8
      pick: 0.19
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.63
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.62
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Gluttonous Grimoire, Amanita Charm, Jotunn''s Revenge,
    Riptalon, The Crusher, Golden Blade, Pharaoh''s Curse, Breastplate of Valor, Soul
    Gem, Freya''s Tears, Oni Hunter''s Garb, Silverbranch Bow, Lernaean Bow, Shogun''s
    Ofuda, Hydra''s Lament, Runeforged Hammer, Spectral Armor, Tyrfing, Erosion, Shield
    Splitter, Spear of the Magus, Eye of Providence, Bracer of The Abyss, Helm of
    Radiance, The Cosmic Horror, Leviathan''s Hide, Eye of the Storm, Yogi''s Necklace,
    Toxic Blade, Midgardian Mail, Death Metal, Mantle Of Discord, Stone of Binding,
    Eros'' Bow, The Reaper.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.54
      win: 0.7
      pick: 0.0
      fit: 0.5
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.59
      win: 0.8
      pick: 0.19
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.58
      efficiency: 0.56
      win: 0.7
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Soul Gem, Gluttonous Grimoire, Freya''s Tears, Amanita Charm, Berserker''s
    Shield, Hydra''s Lament, The Crusher, Oni Hunter''s Garb, Spear of Desolation,
    Chronos'' Pendant, Screeching Gargoyle, Chandra''s Grace, Erosion, Spectral Armor,
    Spear of the Magus, Eye of Providence, Pharaoh''s Curse, Runeforged Hammer, Prophetic
    Cloak, Helm of Radiance, Shield Splitter, The Cosmic Horror, Gem of Focus, Leviathan''s
    Hide, Totem of Death, Eye of the Storm, Rod of Asclepius, Death Metal, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Jade Scepter, Yogi''s Necklace.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.26
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.59
      win: 0.8
      pick: 0.19
      fit: 0.51
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.7
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.7
      pick: 0.0
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Gluttonous Grimoire, Soul Gem, Jotunn''s
    Revenge, Amanita Charm, The Crusher, Berserker''s Shield, Breastplate of Valor,
    Freya''s Tears, Spear of the Magus, The Cosmic Horror, Oni Hunter''s Garb, Hydra''s
    Lament, Death Metal, Helm of Radiance, Spear of Desolation, Rod of Asclepius,
    Runeforged Hammer, Chronos'' Pendant, Shield Splitter, Jade Scepter, Obsidian
    Shard, Spectral Armor, Erosion, Pharaoh''s Curse, Eye of Providence, Eye of the
    Storm, Blood-Bound Book, Bancroft''s Talon, Ethereal Staff, Wish-Granting Pearl,
    Leviathan''s Hide, Bracer of The Abyss, Golden Blade, Triton''s Conch, Midgardian
    Mail, Alchemist Coat.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.59
      win: 0.8
      pick: 0.19
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.63
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.59
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Amanita Charm, Soul Gem, Berserker''s Shield, Breastplate of Valor,
    Freya''s Tears, Spear of the Magus, Oni Hunter''s Garb, Hydra''s Lament, Death
    Metal, The Cosmic Horror, Runeforged Hammer, Helm of Radiance, Shield Splitter,
    Spear of Desolation, Erosion, Spectral Armor, Eye of the Storm, Rod of Asclepius,
    Eye of Providence, Pharaoh''s Curse, Jade Scepter, Obsidian Shard, Chronos'' Pendant,
    Golden Blade, Leviathan''s Hide, Blood-Bound Book, Damaru, Lernaean Bow, The Reaper,
    Bancroft''s Talon, Ethereal Staff, Wish-Granting Pearl, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.27
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.23
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.59
      win: 0.8
      pick: 0.19
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.63
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Gluttonous Grimoire, Jotunn''s Revenge,
    Berserker''s Shield, The Crusher, Freya''s Tears, Breastplate of Valor, Oni Hunter''s
    Garb, Soul Gem, Shield Splitter, Hydra''s Lament, Erosion, Runeforged Hammer,
    Eye of Providence, Eye of the Storm, Spectral Armor, Pharaoh''s Curse, Leviathan''s
    Hide, Spear of the Magus, Golden Blade, Mantle Of Discord, Stone of Binding, Midgardian
    Mail, Death Metal, Helm of Radiance, The Cosmic Horror, Shogun''s Ofuda, Avenging
    Blade, Damaru, Lernaean Bow, The Reaper, Magi''s Cloak, Yogi''s Necklace, Screeching
    Gargoyle, Ancile, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.28
      fit: 0.28
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.59
      win: 0.8
      pick: 0.19
      fit: 0.61
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Gluttonous Grimoire,
    Jotunn''s Revenge, Berserker''s Shield, The Crusher, Freya''s Tears, Breastplate
    of Valor, Oni Hunter''s Garb, Soul Gem, Shield Splitter, Hydra''s Lament, Erosion,
    Runeforged Hammer, Eye of Providence, Eye of the Storm, Spectral Armor, Pharaoh''s
    Curse, Leviathan''s Hide, Spear of the Magus, Golden Blade, Mantle Of Discord,
    Stone of Binding, Midgardian Mail, Death Metal, Helm of Radiance, The Cosmic Horror,
    Shogun''s Ofuda, Avenging Blade, Damaru, Lernaean Bow, The Reaper, Magi''s Cloak,
    Yogi''s Necklace, Screeching Gargoyle, Ancile, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.28
      fit: 0.28
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.59
      win: 0.8
      pick: 0.19
      fit: 0.61
    Gladiator's Shield:
      total: 0.57
      efficiency: 0.41
      win: 0.74
      pick: 0.28
      fit: 0.53
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.51
  swaps:
  - added: Gladiator's Shield
    removed: The Crusher
    reason: community 74% win over 35 matches (vs 54% on this god), taking the model's
      weakest slot from The Crusher
  starter: *id001
---
